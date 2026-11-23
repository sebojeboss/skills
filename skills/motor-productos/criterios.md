# criterios.md — F1/F2: el perfil de caza y el revenue estimado

Leer al entrar a **F1**. Define QUÉ marca clasifica como candidata y CÓMO se estima su facturación.

---

## 1. El arquetipo que buscamos

Una marca **mono-producto en escala media** que un emprendedor puede replicar:

| Señal | Umbral | Por qué |
|---|---|---|
| Catálogo | `max_products_count` ≈ **25** | Mono-producto real. ⚠️ **NO uses 3**: la herramienta cuenta upsells, bundles, gift cards y "protección de envío". Marcas mono-producto reales figuran con **8-22 SKU**. Filtrar en 3 te deja sin resultados. |
| Anuncios activos (piso) | `min_active_ads` ≈ **30** | Deja entrar emergentes (marcas ganadoras arrancan con 40-60 ads). Bajo 30 no hay validación. |
| Anuncios activos (techo) | `max_active_ads` ≈ **1.200** | **Excluye gigantes posicionados** (miles de ads): imposibles de replicar. Sube a ~6.000 solo si buscas el arquetipo "bundle de hogar/lifestyle", que escala más alto. |
| Mercado | `market_countries` = `[MX, CL, CO, AR, PE, ES]` | Mercado hispano: idioma y ángulo directamente transferibles. |
| Momentum | tendencia de anuncios ↑ o tráfico +20%/30d | "En ascenso" — ver §3. |
| Tráfico | **sin piso** | Las emergentes aún no están indexadas. Un piso alto te deja solo con marcas maduras. |

**Ordenar** por `activeAds` (cobertura) y por `growth30d` (momentum), y unir ambos resultados.

---

## 2. Deduplicación (obligatoria)

Las marcas replican tienda por país: `fr.marca.com`, `de.marca.com`, `us.marca.com` son **una sola marca**.

**Regla:** deduplicar por **raíz de dominio** (segundo nivel, ignorando subdominio de país). Sin esto, una marca ocupa 5 filas de tu shortlist y crees que hay más variedad de la que hay.

```python
def raiz(dom):
    p = dom.replace('www.', '').split('.')
    if len(p) >= 3 and len(p[0]) <= 3:  # subdominio de país (fr., de., us.)
        p = p[1:]
    return p[-2] if len(p) >= 2 else dom
```

Cuando una marca aparece varias veces, **quédate con la fila de más anuncios activos**.

---

## 3. "En ascenso" — cómo se calcula

No confíes en el % de crecimiento que entrega la herramienta: viene distorsionado (el último mes suele ser un salto artificial por cómo se indexa el tráfico). **Calcúlalo tú desde el historial de anuncios**:

```
tendencia = (promedio últimas 3 semanas − promedio 3 semanas previas) / (promedio previas + 1)
ascendente = tendencia > 0.10   OR   crecimiento_tráfico_30d > 20%
```

Es la señal más honesta de que la marca está **metiendo presupuesto**, no de que la herramienta reindexó.

---

## 4. Revenue estimado

Estimación gruesa para priorizar (nunca como cifra exacta):

```
compras_mes  = visitas_mes × conversión        (default 3%)
revenue_mes  = compras_mes × precio_SKU_principal
```

**Cómo presentarlo:**
- En **tres columnas separadas** (visitas → compras → revenue), no un número mágico. El usuario debe ver el paso intermedio.
- Deja **compras y revenue como fórmula de Excel** para que el usuario pueda cambiar el 3%.

**Caveats que SIEMPRE se declaran:**
- El 3% aplicado a *todas* las visitas es **generoso** (el promedio real de ecommerce es 1,5-2,5%) → léelo como **techo optimista**.
- El tráfico es aproximación tipo SimilarWeb: en marcas nuevas puede ser 0 o irreal.
- El AOV real suele ser **mayor** que el precio del SKU principal (bundles/upsells).

⚠️ **Señal mixta a reportar:** marca con **muchos anuncios y tráfico ínfimo** (ej. 1.000 ads y 900 visitas). Puede ser marca nueva no indexada o pauta a un mercado no capturado. No la vendas como ganadora sin evidencia extra.

---

## 5. Identificar el SKU principal

El best-seller listado suele traer basura. **Descarta** como "producto hero" cualquier ítem cuyo título contenga:

`gift card`, `tarjeta regalo`, `garantía`, `protección`/`protection`, `shipping`/`envío`, `warranty`, `seguro`, `free gift`/`regalo`, `subscription`/`suscripción`, `bundle` genérico, `certificado de calibración`

Toma el **primer best-seller con precio que sobreviva al filtro**. Si ninguno sobrevive, usa el primero y márcalo para que F3 lo confirme.

---

## 6. Clasificación de tipo y regulación (preliminar)

Etiqueta cada marca para que el usuario vea el peaje regulatorio **antes** de elegir. Reglas completas en [costeo.md](costeo.md) §Regulación; en F2 basta la heurística por título:

| Tipo | Palabras clave | Regulación Chile (preliminar) |
|---|---|---|
| Gadget / Hogar | (resto) | **Ninguna** |
| Cosmético | cream, serum, bálsamo, mascarilla, perfume, maquillaje… | **ISP** |
| Suplemento | cápsula, vitamina, colágeno, probiótico, gomitas… | **SEREMI Salud** |
| Electrónico | recargable, inalámbrico, cepillo eléctrico, cargador… | **SEC** (si es 220V/batería) |
| Textil / Calzado | polera, calza, zapatilla, manta… | Ninguna sanitaria |

Es preliminar: **F3 la corrige con research real**.

---

## 7. Nota de manejo de datos

Las respuestas de `search_shops` son **muy grandes** (100k+ caracteres). Guárdalas en archivo y **parsea con Python**; no las leas completas en contexto. Extrae solo: dominio, nombre, `productsCount`, `activeAds` + historial, `monthlyVisits` + `growth30d`, `topCountries`, `bestSellers`, `createdAt`, `mainCategory`.
