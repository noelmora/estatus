#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import requests

class ChecadorApp(tk.Tk):
    def __init__(self, urls, interval=30):
        super().__init__()
        self.title("🌐 Checador")
        self.urls = urls
        self.interval = interval  # segundos entre cada chequeo
        self.running = True

        self._centra_ventana(800, 400)
        self._configura_estilos()
        self._construye_ui()

        # Hilo de chequeo como daemon para no bloquear la interfaz
        threading.Thread(target=self._bucle_chequeo, daemon=True).start()

        # Manejo de cierre seguro
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _centra_ventana(self, width, height):
        """ Centra la ventana en la pantalla. """
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w - width) // 2
        y = (screen_h - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

    def _configura_estilos(self):
        """ Define estilos para la tabla y filas. """
        style = ttk.Style(self)
        style.theme_use('default')
        style.configure('Treeview', rowheight=24, font=('Segoe UI', 10))
        style.configure('Treeview.Heading',
                        font=('Segoe UI Semibold', 11),
                        background='#333',
                        foreground='white')
        # Colores para filas 
        self.tag_ok = {'background': '#d4edda'}
        self.tag_warn = {'background': '#fff3cd'}
        self.tag_error = {'background': '#f8d7da'}

    def _construye_ui(self):
        """ Crea controles y tabla de estado. """
        top_frame = ttk.Frame(self, padding=10)
        top_frame.pack(fill=tk.X)

        ttk.Label(top_frame, text="Intervalo (s):").pack(side=tk.LEFT)
        self.interval_var = tk.IntVar(value=self.interval)
        spin = ttk.Spinbox(top_frame, from_=5, to=300,
                           textvariable=self.interval_var, width=5)
        spin.pack(side=tk.LEFT, padx=(5,20))
        ttk.Button(top_frame, text="Actualizar Intervalo",
                   command=self._actualiza_intervalo).pack(side=tk.LEFT)

        # Contenedor de la tabla
        table_frame = ttk.Frame(self)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0,10))

        cols = ("Endpoint", "Código", "Tiempo (s)", "Error")
        self.tree = ttk.Treeview(table_frame, columns=cols, show='headings')
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.W, width=180)

        vsb = ttk.Scrollbar(table_frame, orient="vertical",
                             command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Filas iniciales
        for url in self.urls:
            self.tree.insert('', tk.END, iid=url, values=(url, '-', '-', '-'))

    def _actualiza_intervalo(self):
        """ Ajusta el intervalo de chequeos. """
        val = self.interval_var.get()
        if val < 5:
            messagebox.showwarning("Valor inválido",
                                   "El intervalo mínimo es 5 segundos.")
            return
        self.interval = val
        messagebox.showinfo("Intervalo actualizado",
                             f"Nuevo intervalo: {self.interval}s")

    def _bucle_chequeo(self):
        #Bucle en segundo plano que realiza el chequeo de endpoints y actualiza la tabla 
        
        while self.running:
            for url in self.urls:
                code, elapsed, err = self._checar_url(url)
                self.after(0, self._actualizar_fila,
                           url, code, elapsed, err)
            # Espera segura entre chequeos
            for _ in range(self.interval):
                if not self.running:
                    break
                time.sleep(1)

    def _checar_url(self, url, timeout=5.0):
        #Realiza GET a la URL y devuelve status, tiempo, error
        try:
            start = time.time()
            r = requests.get(url, timeout=timeout)
            elapsed = f"{time.time() - start:.2f}"
            return r.status_code, elapsed, ''
        except Exception as e:
            return None, None, str(e)

    def _actualizar_fila(self, url, status, elapsed, error):
         #Actualiza los datos y color de la fila correspondiente
        code = status if status is not None else '-'
        t = elapsed if elapsed is not None else '-'
        err = error or '-'
        self.tree.item(url, values=(url, code, t, err))

        # Asigna color según estado
        if status == 200:
            self.tree.item(url, tags=('ok',))
        elif status is None:
            self.tree.item(url, tags=('error',))
        else:
            self.tree.item(url, tags=('warn',))

        # Configura etiquetas de estilo
        self.tree.tag_configure('ok', **self.tag_ok)
        self.tree.tag_configure('warn', **self.tag_warn)
        self.tree.tag_configure('error', **self.tag_error)

    def _on_close(self):
        #Detiene el bucle y cierra la aplicación
        self.running = False
        self.destroy()


if __name__ == '__main__':
    endpoints = [
        'http://localhost:8000/servidor',
        'https://www.google.com/',
        'https://api.telegram.org/',
         
    ]
    app = ChecadorApp(endpoints, interval=30)
    app.mainloop()
