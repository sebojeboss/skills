# research.md — F3: research profundo por producto

Leer al entrar a **F3**, solo sobre los productos que el usuario marcó **"Sí"**.

⚠️ **Regla marco: NO te limites al ad-spy.** F3 es **research web profundo multi-fuente**. TrendTrack es *una* fuente; el grueso sale de Google, marketplaces locales, redes y Alibaba/1688.

---

## 1. Arquitectura: 2 etapas por producto

Un producto = **2 agentes en cadena**:

1. **Research** (esfuerzo alto): investiga y llena el esquema.
2. **Verificación adversarial** (esfuerzo medio): intenta **refutar** el brief anterior con sus propias búsquedas y lo corrige.

La etapa 2 no es cosmética: en corridas reales corrigió cosas como *"el producto no es un spray, es una camisa"*, *"la autoridad no es el ISP sino la SEREMI"* y *"ese ángulo ya existe en góndola, no hay hueco"*.

**Paraleliza por producto** (pipeline), no por etapa: cada producto avanza a verificación apenas termina su research, sin esperar a los demás.

---

## 2. Qué debe entregar cada brief (esquema)

| Campo | Contenido |
|---|---|
| `heroProductReal` / `isPhysical` | **Qué se vende de verdad.** Si el best-seller parece ebook/"método", buscar el producto físico detrás. Si es 100% digital, marcarlo (no aplica costeo). |
| `whatItIs`, `funnelAngle` | Qué es y qué promete, a quién apunta. |
| `chileCompetitors[]` | **2-5 competidores con URL real** (nombre, link, nota con precio local). |
| `competitorSummary` | ¿Saturado o hay hueco? Con precios de referencia locales. |
| `dtcDesire` | El deseo profundo/emocional que mueve la compra (no el beneficio funcional). |
| `dtcOpportunity` | La oportunidad concreta en el destino: qué hueco, qué ángulo, por qué pegaría. |
| `regulatoryChile` | ISP / SEREMI / SEC / SAG / ninguna — con el porqué. |
| `alibabaReferences[]`, `fobUnitUsdLow/High`, `moq`, `weightKg`, `dimsCm` | Sourcing: referencias con URL, rango FOB, MOQ, **peso y dimensiones** (insumo directo de F4). |
| `sourcingNotes` | **Qué es dato encontrado vs estimación.** Obligatorio. |
| `confidence` | alta / media / baja. |
| `sources[]` | URLs consultadas. |

Forzar el esquema con **structured output**: garantiza que `weightKg`, `dimsCm` y el rango FOB **siempre** vengan (F4 los necesita para calcular).

---

## 3. Dónde buscar competencia local (Chile)

Google + **MercadoLibre.cl** + Falabella + Paris + Sodimac/Easy (hogar) + Preunic/DBS (belleza) + tiendas Shopify locales + Instagram CL.

Buscar el **producto genérico**, no la marca: la marca gringa no está en Chile, pero **el producto sí suele estar** — y a menor precio. Ese es el dato que decide.

---

## 4. Sourcing: qué esperar de Alibaba

- **Alibaba bloquea el fetch de fichas individuales.** Es normal que el agente no pueda abrir el SKU exacto. Entonces: usar precios visibles en resultados de búsqueda, showrooms y análogos, y **declararlo como estimación** en `sourcingNotes`.
- **El FOB depende del volumen**: a MOQ 100 es 2-3× más caro que a 1.000-5.000. Pedir siempre **rango** (`Low` = precio a volumen, `High` = MOQ bajo). F4 usa el de volumen.
- Ojo con confundir **precio retail con FOB**: si el "FOB" se parece al precio de Amazon, está mal.
- Para suplementos y cosméticos, el sourcing es **private label / OEM** (frasco terminado con tu etiqueta), no un SKU suelto.

---

## 5. Reglas anti-invención

1. **Competidor sin URL no existe.** Si no puedes linkearlo, no lo listes.
2. **Nunca inventes un FOB "redondo" sin respaldo.** Si es estimación, escribe *estimación por categoría* y de qué análogo sale.
3. **Si una página no carga, dilo** — pero igual entrega el número estimado (F4 lo necesita) marcado como estimación.
4. **Baja `confidence` cuando corresponda.** Un brief honesto en "media" vale más que uno inflado en "alta".
5. **Corrige el supuesto del usuario si el dato lo contradice** (producto mal identificado, autoridad regulatoria equivocada, hueco inexistente). Eso es el valor de esta fase.

---

## 6. Costo de la fase

~2 agentes por producto. **12 productos ≈ 24 agentes.** Es el gasto grande del motor: confirma el alcance con el usuario en F0 antes de lanzar.

---

## 7. Salida

Guardar los briefs verificados como **`briefs.json`** en la carpeta del caso. Es el insumo directo de F4 (costeo) y F5 (entregables).
