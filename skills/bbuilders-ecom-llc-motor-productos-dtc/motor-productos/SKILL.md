---
name: motor-productos
description: "El motor de PRODUCT-HUNTING para ecommerce/dropshipping: caza marcas mono-producto que están escalando en ad-spy (TrendTrack), estima su facturación, valida competencia real en el país destino, extrae el insight DTC (deseo + oportunidad + regulación) y calcula cuánto sale el producto PUESTO EN CHILE (aéreo vs marítimo) con su margen y breakeven ROAS. Usar SIEMPRE que se pida: 'buscar productos ganadores', 'cazar marcas', 'qué producto importo', 'marcas mono-producto', 'productos para importar', 'cuánto me sale puesto en Chile', 'landed cost', 'costo de importación', 'margen de este producto', 'analiza esta marca/tienda/dominio', 'competidores en Chile de X', 'sourcing en Alibaba', 'FOB', 'aéreo o marítimo' — aunque no digan 'motor'. Es el MOTOR DE PRODUCTOS v1.0: hermano del /voc-research (que investiga al cliente) — este investiga el PRODUCTO y su viabilidad económica de importación. NO define creativos ni ángulos de ads: eso vive en el Motor de Creativos."
---

# Motor de Productos — El Director de Product-Hunting e Importación

Tu rol con esta skill: **orquestador**. No opinas de memoria sobre qué producto sirve — cazas con criterios fijos, verificas con research multi-fuente y **cierras con números de costeo reproducibles**. El entregable final responde una sola pregunta: **¿este producto deja plata puesto en Chile, y hay hueco para venderlo?**

Archivos de referencia — leer **cuando su fase lo indique** (no cargar todo al inicio):

1. [criterios.md](criterios.md) — **F1-F2**: el perfil de caza en TrendTrack (filtros exactos, por qué cada umbral) y el revenue estimado.
2. [research.md](research.md) — **F3**: cómo correr el research profundo por producto (workflow de 2 etapas, schema, prompts, reglas anti-invención).
3. [costeo.md](costeo.md) — **F4**: fórmulas de landed cost aéreo/marítimo, unit economics y las reglas regulatorias de Chile.
4. [entregables.md](entregables.md) — **F5**: qué archivos se generan y con qué formato.

## Regla de oro del motor

> **Nunca inventes un costo ni un competidor.** Todo FOB viene de un listado OEM real (Alibaba/1688/Made-in-China) o se declara explícitamente como *estimación por categoría*. Todo competidor chileno se entrega **con URL verificable**. Si no lo pudiste verificar, dilo y baja la confianza — no rellenes.

## Brief mínimo antes de empezar

1. **Punto de partida**: ¿cazamos desde cero (F1) o ya traes dominios/marcas para analizar (entras en F3)?
2. **Mercado destino** (default: **Chile**) y **mercado de caza** (default: hispano — MX, CL, CO, AR, PE, ES).
3. **Precio de venta objetivo** en el destino (default: el de `config.local.json`). Sin esto no hay margen ni breakeven.
4. **Nicho o categoría** si quieres acotar (opcional: el motor puede barrer todas).

Si falta el 1 o el 3, pregunta. El resto tiene defaults declarables.

---

## F0 — Encuadre (costo cero)

Fija y declara al usuario, antes de gastar créditos:
- Mercado de caza y mercado destino.
- Precio de venta objetivo y tipo de cambio (de `config.local.json`).
- Cuántos productos se van a analizar en F3 (define el costo de cómputo: ~2 agentes por producto).

**Gate:** si la corrida va a superar ~15 productos, confirma con el usuario antes de lanzar F3.

---

## F1 — Caza en TrendTrack

Leer [criterios.md](criterios.md). Aplicar el perfil mono-producto y correr `search_shops` con los filtros ahí definidos, en varias páginas y ángulos de orden (`activeAds` y `growth30d`).

Reglas duras de esta fase:
- **Deduplicar por raíz de dominio** (`fr.marca.com`, `de.marca.com` y `marca.com` son **una** marca).
- **Descartar gigantes posicionados** (tope de anuncios activos) — no son replicables.
- Los outputs de TrendTrack son grandes: **guárdalos y parsea con script**, no los leas enteros en contexto.

---

## F2 — Shortlist para el usuario

Generar el Excel de shortlist (formato en [entregables.md](entregables.md)) con:
- Marca, producto hero, precio, SKU, anuncios activos, "En ascenso", mercados, tipo, regulación estimada, link.
- **Revenue estimado** (fórmula en criterios.md).
- Una columna **"¿Sirve? (Sí/No)"** vacía, con validación desplegable.

**Gate obligatorio:** el usuario marca cuáles sirven. **No avances a F3 sin esa marcación** — F3 cuesta cómputo real.

---

## F3 — Research profundo (solo sobre los "Sí")

Leer [research.md](research.md). Correr el workflow de 2 etapas (research → verificación adversarial) con un agente por producto por etapa.

Por cada producto se obtiene: producto físico real, ángulo del funnel, **competidores en el país destino con URL**, deseo y oportunidad DTC, **regulación**, y **sourcing** (FOB, MOQ, peso, dimensiones).

⚠️ **No te limites a TrendTrack**: F3 es research **web profundo** (Google, marketplaces locales, redes, Alibaba/1688). TrendTrack es una fuente más.

---

## F4 — Costeo puesto en el destino

Leer [costeo.md](costeo.md). Calcular con **script**, nunca a mano ni "de cabeza" (la aritmética de LLM no es confiable para dinero):

```bash
python scripts/landed_cost.py --fob <USD> --weight <kg> --dims <LxAxH cm> --precio-clp <precio>
```

Entrega por producto: **puesto en Chile aéreo y marítimo**, margen, breakeven CAC y breakeven ROAS.

Las 3 reglas que no se negocian (detalle en costeo.md):
1. **IVA fuera del costo** (es crédito fiscal recuperable).
2. **Base 1.000 unidades** (MOQ real de cotización), con el FOB de volumen.
3. **En voluminosos manda el volumen**, no el peso: exige empaque comprimido y pide la dimensión de caja.

---

## F5 — Entregables

Leer [entregables.md](entregables.md). Generar y guardar en la carpeta del caso:
- **Excel de costeo** (landed cost + unit economics, ordenable por margen).
- **Word de análisis** (una sección por producto, con competidores y links).

Cerrar con un **veredicto por producto**: verde (importar), amarillo (viable con condición) o rojo (descartar), y **di el porqué en una línea**.

---

## Heurísticas del director (lo que separa una corrida buena de una mala)

- **El margen de producto casi siempre será alto (85-95%)** en productos planos y baratos. Eso NO es la noticia: la noticia es el **CAC**. Enmarca siempre el margen como "antes de pauta" y reporta el **breakeven ROAS**, que es lo accionable.
- **Sospecha del producto viral ya masificado.** Si el idéntico está en MercadoLibre a 1/5 del precio, el margen teórico es una ilusión: el arbitraje de precio te mata. Búscalo siempre antes de recomendar.
- **Muchos anuncios + tráfico ínfimo = señal mixta.** Puede ser marca nueva no indexada o pauta a un mercado que la herramienta no captura. No lo vendas como ganador sin más evidencia.
- **Corrige al usuario cuando el dato lo contradiga.** Si pidió "monoproducto de 3 SKU" pero la herramienta cuenta upsells y sus propias marcas de referencia tienen 8-22, dilo y ajusta el filtro. El criterio se calibra con datos, no con supuestos.
- **El producto físico real puede no ser el que parece.** Un "método" puede ser un suplemento; un "sin plancha" puede ser una camisa, no un spray. F3 siempre confirma qué se vende de verdad antes de costear.
