# costeo.md — F4: landed cost, unit economics y regulación

Leer al entrar a **F4**. Es la fase donde el motor gana o pierde credibilidad: **cálculo siempre por script**, nunca a mano.

```bash
python scripts/landed_cost.py --fob 9 --weight 1.4 --dims 42x33x16 --precio-clp 44990
```

---

## 1. Las 3 reglas que no se negocian

### 1.1 El IVA NO es costo
El IVA 19% se paga al importar, pero para una empresa con RUT es **crédito fiscal recuperable**: lo descuentas del IVA que cobras al vender. **Meterlo en el costo unitario infla todo ~19% y te hace descartar productos buenos.**

→ Calcúlalo y **muéstralo en columna aparte** ("IVA recuperable"), nunca dentro del costo.

### 1.2 Base 1.000 unidades
Los proveedores OEM **cotizan sobre 1.000 unidades como mínimo**. Costear con el FOB de MOQ 100 te da un costo 2-3× más caro que el real y mata productos viables.

→ Ambos escenarios (aéreo y marítimo) usan el **FOB de volumen**. Lo único que cambia entre ellos es el **flete**.

### 1.3 En voluminosos manda el volumen, no el peso
Un peluche de 1,4 kg puede pagar flete como si pesara 13 kg (peso volumétrico). **El empaque comprimido decide si el negocio existe.**

→ Exige **empaque al vacío** en la cotización y pide la **dimensión exacta de la caja comprimida**. Ese solo número puede mover el margen 20 puntos.

---

## 2. Fórmulas

**Peso facturable aéreo** (el que cobra el courier):
```
peso_volumétrico = (L × A × H cm) / 6000
peso_facturable  = max(peso_real, peso_volumétrico)
flete_aéreo/u    = peso_facturable × tarifa_aérea      (default US$6/kg)
```

**Flete marítimo (LCL)**:
```
volumen_m3/u   = (L × A × H cm) / 1.000.000
volumen_total  = volumen_m3 × 1.000 u        (mínimo facturable: 1 m³)
flete_marítimo/u = max(1, volumen_total) × tarifa_marítima / 1.000   (default US$200/m³)
```

**Puesto en destino, por unidad**:
```
CIF     = FOB + flete + seguro (1,5% del FOB)
landed  = CIF × (1 + arancel 6%) + despacho (US$0,30/u)
IVA_rec = CIF × 1,06 × 19%        ← aparte, recuperable, NO se suma
```

**Unit economics** (precio de venta CON IVA, ej. $34.990 CLP):
```
neto        = precio / 1,19
landed_CLP  = landed_USD × tipo_cambio
margen/u    = neto − landed_CLP
margen %    = margen / neto
breakeven CAC   = margen/u          ← lo máximo que puedes pagar por venta
breakeven ROAS  = precio / margen/u ← sobre esto, ganas
```

---

## 3. Cómo interpretar el resultado

- **Margen de producto 85-95% es lo NORMAL** en productos planos y baratos. No es la noticia. La noticia es el **breakeven ROAS**.
- **Breakeven ROAS < 2** = mucho aire para escalar. **Entre 2 y 3** = exige eficiencia. **> 3** = producto frágil, el flete o el FOB se están comiendo el negocio.
- Presenta siempre la **escalera de precio** (3 precios de venta) para que el usuario vea cuánto margen compra cada tramo. Regla útil: cada +$5.000 CLP de precio suma ~$4.200 CLP de margen neto por unidad.
- **Aéreo vs marítimo**: en productos **livianos y planos** el aéreo cuesta casi lo mismo por unidad → puedes importar rápido sin castigar margen. En **voluminosos**, el aéreo se descarta solo.

---

## 4. Regulación en Chile (verificado)

⚠️ **El error más común es mandar todo al ISP.** No es así:

| Producto | Autoridad | Qué implica |
|---|---|---|
| **Suplemento alimenticio** | **SEREMI de Salud** (Reglamento Sanitario de los Alimentos, D.S. 977/1996) — **no ISP** | Autorización de uso y disposición en cada importación. Pasa a **ISP** (control tipo farmacéutico) **solo si declara propiedades terapéuticas**. |
| **Cosmético** (crema, mascarilla, maquillaje, perfume) | **ISP** | Registro sanitario de cosmético (D.S. 239/02), representante legal en Chile, fórmula cuali-cuantitativa. Vigencia 5 años. |
| **Eléctrico 220V / con cargador** | **SEC** | Certificación obligatoria del **cargador/adaptador de pared**. Truco: importar **sin adaptador de pared** (solo cable USB) reduce mucho la exposición. Batería de litio → reglas IATA/UN38.3 para el flete aéreo. |
| **Repelente / agroquímico** | **SAG / ISP** | Revisar antes de comprometer volumen. |
| **Textil, calzado, equipaje, juguete** | **Ninguna sanitaria** | Solo arancel + IVA. Juguete: pedir certificado de seguridad (CE) al proveedor. |

**Regla de marketing que cuesta caro ignorar:** en Chile **están prohibidos los claims terapéuticos o de cura** en etiqueta y publicidad ("elimina el dolor", "cura la inflamación"). Los ángulos agresivos de los funnels gringos **hay que suavizarlos** a lenguaje de bienestar.

---

## 5. Trampa del arbitraje de precio

Antes de recomendar cualquier producto: **búscalo en MercadoLibre y retail local**. Si el idéntico ya se vende a 1/5 del precio del funnel original, el margen teórico es una ilusión — no puedes sostener el premium sin una marca fuerte. Repórtalo como **riesgo rojo** aunque el margen calculado sea 95%.

---

## 6. Qué declarar siempre

Toda cifra de costeo se entrega con su origen:
- **FOB**: ¿listado OEM real (con URL) o estimación por categoría? Dilo.
- **Peso y dimensiones**: ¿dato del proveedor o estimación? Dilo.
- **Fletes y tipo de cambio**: son supuestos de `config.local.json` — recuérdale al usuario actualizarlos con sus cotizaciones reales.

> Un costeo con supuestos declarados es útil. Un costeo que finge precisión es peligroso.
