import os
import re
import time
import pdfplumber
import pandas as pd
import customtkinter as ctk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURAÇÕES DO SISTEMA ---
PASTA_MONITORADA = "./faturas_entrada"
ARQUIVO_EXCEL = "Relatorio_Financeiro.xlsx"

def processar_pdf(caminho_pdf):
    try:
        time.sleep(1.5) 
        with pdfplumber.open(caminho_pdf) as pdf:
            texto = pdf.pages[0].extract_text()
            if not texto: return {"Erro": "PDF sem texto"}

            # --- REGEX PARA O ID ---
            # Procura por "Fatura", "Nº", "Doc" seguido de números/letras
            padrao_id = r"(?:Fatura|N.º|Nº|Documento)\s*[:#]?\s*([A-Z0-9\-/]+)"
            match_id = re.search(padrao_id, texto, re.IGNORECASE)
            id_fatura = match_id.group(1) if match_id else "Não encontrado"

            # --- REGEX PARA O VALOR ---
            # Procura por padrões como 1.234,56 ou 1234.56 ou 45,00
            # Focamos no valor que vem depois de "Total" ou "Valor"
            padrao_valor = r"(?:Total|Valor|Pagar)\s*(?:[A-Z$€ ]+)?\s*([\d\.\,]+)"
            match_valor = re.search(padrao_valor, texto, re.IGNORECASE)
            valor = match_valor.group(1) if match_valor else "0,00"

            return {
                "Data": time.strftime("%d/%m/%Y"), 
                "Ficheiro": os.path.basename(caminho_pdf), 
                "ID": id_fatura,
                "Valor": valor
            }
    except Exception as e:
        return {"Erro": str(e)}

def salvar_no_excel(dados):
    try:
        if os.path.exists(ARQUIVO_EXCEL):
            df_antigo = pd.read_excel(ARQUIVO_EXCEL)
            df_novo = pd.concat([df_antigo, pd.DataFrame([dados])], ignore_index=True)
        else:
            df_novo = pd.DataFrame([dados])
        
        df_novo.to_excel(ARQUIVO_EXCEL, index=False)
        return True
    except PermissionError:
        return "Erro: O arquivo Excel está aberto! Feche-o para salvar."
    except Exception as e:
        return f"Erro ao salvar: {e}"

class MonitoradorHandler(FileSystemEventHandler):
    def __init__(self, app):
        self.app = app

    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(".pdf"):
            # Usamos after() para garantir que a GUI atualiza na thread certa
            self.app.after(100, self.app.adicionar_log, f"📄 Novo arquivo detectado: {os.path.basename(event.src_path)}")
            
            dados = processar_pdf(event.src_path)
            resultado = salvar_no_excel(dados)
            
            if resultado == True:
                self.app.after(200, self.app.adicionar_log, "✅ Dados salvos com sucesso!")
            else:
                self.app.after(200, self.app.adicionar_log, f"❌ {resultado}")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Automação de Faturas")
        self.geometry("600x450")

        self.label = ctk.CTkLabel(self, text="Monitor de Documentos Inteligente", font=("Roboto", 22, "bold"))
        self.label.pack(pady=20)

        self.btn_status = ctk.CTkButton(self, text="Iniciar Monitoramento", command=self.toggle_monitor, fg_color="green")
        self.btn_status.pack(pady=10)

        self.btn_abrir_excel = ctk.CTkButton(self, text="Abrir Relatório Excel", command=self.abrir_excel, fg_color="#333333")
        self.btn_abrir_excel.pack(pady=5)

        self.log_text = ctk.CTkTextbox(self, width=500, height=200)
        self.log_text.pack(pady=20)
        self.log_text.insert("0.0", "Aguardando início...\n")

        self.observer = None
        self.rodando = False

    def adicionar_log(self, mensagem):
        self.log_text.insert("end", f"[{time.strftime('%H:%M:%S')}] {mensagem}\n")
        self.log_text.see("end")

    def toggle_monitor(self):
        if not self.rodando:
            if not os.path.exists(PASTA_MONITORADA): 
                os.makedirs(PASTA_MONITORADA)

            self.rodando = True
            self.btn_status.configure(text="Parar Monitoramento", fg_color="red")
            self.adicionar_log(f"🚀 Monitorando: {PASTA_MONITORADA}")

            self.observer = Observer()
            # Passamos a instância 'self' para o handler
            handler = MonitoradorHandler(self)
            self.observer.schedule(handler, PASTA_MONITORADA, recursive=False)
            self.observer.start()
        else:
            self.rodando = False
            self.btn_status.configure(text="Iniciar Monitoramento", fg_color="green")
            if self.observer:
                self.observer.stop()
                self.observer.join()
            self.adicionar_log("🛑 Monitoramento parado.")

    def abrir_excel(self):
        if os.path.exists(ARQUIVO_EXCEL):
            os.startfile(ARQUIVO_EXCEL)
        else:
            self.adicionar_log("❌ O Excel ainda não existe.")

if __name__ == "__main__":
    app = App()
    app.mainloop()