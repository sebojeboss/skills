# entregables.md — F5: qué se entrega y con qué formato

Leer al entrar a **F5**. Todo va a la carpeta del caso (`casos/<AAAA-MM>-<nicho>/`).

---

## 1. Shortlist de caza (F2) — `shortlist.xlsx`

```bash
python scripts/build_shortlist_xlsx.py shops.json shortlist.xlsx --precio-clp 34990
```

| Columna | Nota |
|---|---|
| # · Marca · Producto hero · Precio | del best-seller filtrado (criterios.md §5) |
| Nº SKU · Ads activos · **En ascenso** | "En ascenso" resaltado en verde |
| Visitas/mes · Compras est. · **Revenue est.** | compras y revenue **como fórmula** (editable) |
| Creada · Mercados · Tipo · Regulación CL | peaje regulatorio visible antes de elegir |
| Link | clickeable |
| **¿Sirve? (Sí/No)** | **vacía**, con desplegable Sí/No/Tal vez, celda amarilla |

Con **filtro automático**, **panel congelado** y **máx. 1 fila por marca**.

> Esta hoja es un **gate**: el usuario la marca y recién ahí se corre F3.

---

## 2. Excel de costeo (F5) — `RESUMEN_costeo.xlsx`

```bash
python scripts/build_costeo_xlsx.py briefs.json RESUMEN_costeo.xlsx --precio-clp 34990
```

Columnas: Marca · Producto real · Tipo · **FOB @1.000u** · **Puesto CL aéreo/u** · **Puesto CL marítimo/u** (resaltado) · **IVA recuperable** · Precio venta · **Margen** · **Breakeven ROAS** · Competencia (Saturado/Hueco) · Regulación · Confianza · Link.

Ordenado por margen. Nota al pie con los supuestos usados (fletes, TC, base 1.000u, IVA recuperable).

---

## 3. Word de análisis (F5) — `ANALISIS.docx`

```bash
python scripts/build_analisis_docx.py briefs.json ANALISIS.docx --precio-clp 34990
```

Estructura:
1. **Portada + metodología** (research multi-fuente, base 1.000u, IVA recuperable, TC).
2. **Tabla de ranking** por margen, con regulación.
3. **Una sección por producto** (salto de página):
   - Producto real · Qué es · Ángulo del funnel
   - **Competencia en Chile** — resumen + lista de competidores **con links**
   - **Insight DTC** — deseo · oportunidad · regulación
   - **Sourcing** — referencias Alibaba, FOB, MOQ, peso, dimensiones + notas de estimación
   - **Puesto en Chile + unit economics** — aéreo, marítimo, margen, breakeven ROAS

> **Entrega en Word, no en Markdown.** El `.md` sirve como fuente, pero el cliente/alumno lee y comparte `.docx`.

---

## 4. Veredicto (obligatorio al cerrar)

Cierra siempre con un semáforo de una línea por producto:

- 🟢 **Verde** — importar: margen sano, hueco real, sin traba regulatoria.
- 🟡 **Amarillo** — viable **con condición** (ej.: *"solo por barco y con empaque al vacío"*, *"solo si tramitas ISP"*).
- 🔴 **Rojo** — descartar, y **por qué en una línea** (ej.: *"el idéntico está en MercadoLibre a 1/5 del precio"*).

Sin veredicto, el entregable es data, no decisión.

---

## 5. Convención de archivos

```
casos/<AAAA-MM>-<nicho>/
├── shops.json            ← crudo de la caza (F1)
├── shortlist.xlsx        ← F2 (con tu columna ¿Sirve?)
├── briefs.json           ← F3 verificado
├── RESUMEN_costeo.xlsx   ← F5
└── ANALISIS.docx         ← F5
```

**Nunca sobrescribas un archivo que el usuario está editando.** Si Windows lo bloquea (`PermissionError`), avísale que lo cierre en vez de guardar una copia con otro nombre — se pierde la trazabilidad y sus marcas.
