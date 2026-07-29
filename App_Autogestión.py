import io
import os
import pandas as pd
import streamlit as st

# ==========================================
# CONFIGURACIÓN DE PÁGINA
# ==========================================
st.set_page_config(
    page_title="Auditor-IA Costos Tercerizados TigoUNE",
    page_icon="🏢",
    layout="wide",
)

# ==========================================
# ESTILOS CSS PERSONALIZADOS (MANUAL DE MARCA CASALIMPIA)
# ==========================================
st.markdown(
    """
    <style>
        /* Importar fuente oficial Montserrat */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap');

        .stApp { background-color: #f1f5f9; }

        /* Contenedor tipo "Hoja/Página" amplio */
        .block-container {
            max-width: 1550px !important;
            padding: 35px 50px !important;
            background-color: #ffffff;
            border: 2px solid #cbd5e1;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
            margin-top: 20px;
            margin-bottom: 35px;
        }

        /* Tipografía oficial */
        html, body, [class*="css"] {
            font-family: 'Montserrat', sans-serif !important;
            color: #1e293b;
        }

        /* BANNER INSTITUCIONAL DE ENCABEZADO CON LOGO COMPLETO */
        .header-brand {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: linear-gradient(135deg, #f0f7fc 0%, #ffffff 100%);
            padding: 20px 30px;
            border-radius: 10px;
            border-left: 7px solid #1179bf;
            margin-bottom: 25px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.04);
            border-right: 1px solid #e2e8f0;
            border-top: 1px solid #e2e8f0;
            border-bottom: 1px solid #e2e8f0;
        }
        .header-brand-content {
            display: flex;
            align-items: center;
            gap: 25px;
        }
        .header-brand img {
            height: 65px;
            width: auto;
            object-fit: contain;
        }
        .header-brand .title-text h1 {
            color: #1179bf !important;
            font-weight: 800;
            margin: 0;
            font-size: 1.9rem;
            letter-spacing: -0.5px;
        }
        .header-brand .title-text p {
            color: #555;
            margin: 3px 0 0 0;
            font-size: 0.98rem;
            font-weight: 500;
        }

        h2, h3, .section-header {
            color: #83b431 !important;
            font-weight: 700 !important;
        }

        .card-box {
            background-color: #f8f9fa;
            border: 1px solid #e2e8f0;
            padding: 22px;
            border-radius: 10px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
            margin-bottom: 15px;
        }

        /* Top Bar de Resumen Financiero */
        .summary-bar {
            background-color: #1e293b;
            color: white;
            border-radius: 10px;
            padding: 15px 25px;
            display: flex;
            justify-content: space-around;
            align-items: center;
            margin-bottom: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        }
        .summary-item {
            text-align: center;
        }
        .summary-item .label {
            font-size: 0.78rem;
            color: #94a3b8;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 0.5px;
        }
        .summary-item .value {
            font-size: 1.45rem;
            font-weight: 800;
            color: #ffffff;
            margin-top: 2px;
        }

        /* Botones Principales */
        div.stButton > button[kind="primary"], div.stDownloadButton > button[kind="primary"] {
            background-color: #1179bf !important;
            color: white !important;
            border: none !important;
            font-size: 1.05rem !important;
            font-weight: 700 !important;
            border-radius: 8px !important;
            padding: 12px 24px !important;
            min-height: 50px !important;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(17, 121, 191, 0.2);
        }
        
        div.stButton > button[kind="primary"]:hover, div.stDownloadButton > button[kind="primary"]:hover {
            background-color: #0e629b !important;
            box-shadow: 0 6px 12px rgba(14, 98, 155, 0.3);
            transform: translateY(-1px);
        }

        .badge-success {
            background-color: #eaf5d8;
            color: #4b6e19;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 0.88rem;
            font-weight: 600;
            display: inline-block;
            margin-top: 8px;
            border: 1px solid #c2e28f;
        }

        /* TARJETAS KPI MINIMALISTAS CON SUBTEXTO DE DINERO */
        .kpi-card-exec {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 14px 12px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.03);
            text-align: center;
            min-height: 135px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .kpi-card-exec h4 {
            font-size: 0.78rem !important;
            font-weight: 700 !important;
            margin: 0 0 4px 0 !important;
            line-height: 1.2;
            text-transform: uppercase;
            letter-spacing: 0.2px;
        }

        .kpi-card-exec .kpi-num {
            font-size: 1.8rem;
            font-weight: 800;
            line-height: 1;
            margin: 4px 0;
        }

        .kpi-card-exec .kpi-money {
            font-size: 0.85rem;
            font-weight: 700;
            color: #64748b;
            border-top: 1px dashed #cbd5e1;
            padding-top: 4px;
            margin-top: 4px;
        }

        /* Bordes superiores diferenciadores */
        .border-total { border-top: 5px solid #1e293b; }
        .border-total h4 { color: #1e293b !important; }
        .border-total .kpi-num { color: #1e293b; }

        .border-correcto { border-top: 5px solid #83b431; }
        .border-correcto h4 { color: #58801d !important; }
        .border-correcto .kpi-num { color: #83b431; }

        .border-nocobro { border-top: 5px solid #e11d48; }
        .border-nocobro h4 { color: #be123c !important; }
        .border-nocobro .kpi-num { color: #e11d48; }

        .border-perdida { border-top: 5px solid #f97316; }
        .border-perdida h4 { color: #c2410c !important; }
        .border-perdida .kpi-num { color: #f97316; }

        .border-sinreq { border-top: 5px solid #1179bf; }
        .border-sinreq h4 { color: #0e629b !important; }
        .border-sinreq .kpi-num { color: #1179bf; }

        hr { border-top: 2px solid #e2e8f0; margin: 30px 0; }
    </style>
""",
    unsafe_allow_html=True,
)

CARPETA_DESTINO = (
    r"C:\Users\ayrodriguezc.ORGCASALIMPIA\Downloads\Archivos para n8n"
)
RUTA_ARCHIVO_DEPURADO = os.path.join(CARPETA_DESTINO, "BBDD para análisis.xlsx")

MAPA_ESTADOS = {
    "SIN FACTURAR AL CLIENTE": "Facturación del proveedor sin cobro al cliente",
    "A PERDIDA": "Facturación del proveedor con pérdida",
    "SIN NOVEDAD": "Gestión correcta",
    "SIN REQUERIMIENTO": (
        "Facturación del proveedor sin requerimientos identificados"
    ),
}


def guardar_archivo(uploaded_file):
  if uploaded_file is not None:
    os.makedirs(CARPETA_DESTINO, exist_ok=True)
    filepath = os.path.join(CARPETA_DESTINO, uploaded_file.name)
    with open(filepath, "wb") as f:
      f.write(uploaded_file.getbuffer())
    return filepath
  return None


# ==========================================
# LÓGICA DE PROCESAMIENTO PURE PYTHON
# ==========================================
def procesar_cruce_python(
    r_novasoft,
    r_reversiones,
    r_cuadro,
    r_fact_nova,
    r_dian,
    carpeta_salida,
    ruta_excel_salida,
):
  def clean_key(val):
    if pd.isna(val) or val is None:
      return ""
    s = str(val).strip()
    if s.endswith(".0"):
      s = s[:-2]
    return s if s not in ["nan", "None"] else ""

  def es_requerimiento_valido(val):
    s = clean_key(val)
    if not s or s == "0":
      return False
    if not s.isdigit():
      return False
    return True

  # 1. Cargar Excels
  df_costos = pd.read_excel(r_novasoft)
  df_rev = pd.read_excel(r_reversiones)
  df_cuadro = pd.read_excel(r_cuadro)
  df_fnova = pd.read_excel(r_fact_nova)
  df_dian = pd.read_excel(r_dian)

  for df in [df_costos, df_rev, df_cuadro, df_fnova, df_dian]:
    df.columns = df.columns.astype(str).str.strip()

  # 2. Procesar Reversiones
  col_val_fact = None
  for col in df_rev.columns:
    if "FACTURADO" in col.upper() or "VALOR" in col.upper():
      col_val_fact = col
      break
  if not col_val_fact:
    col_val_fact = df_rev.columns[-1]

  col_rq_rev = (
      "RQ"
      if "RQ" in df_rev.columns
      else [c for c in df_rev.columns if "RQ" in c.upper()][0]
  )
  df_rev["RQ_CLEAN"] = df_rev[col_rq_rev].apply(clean_key)
  df_rev[col_val_fact] = pd.to_numeric(df_rev[col_val_fact], errors="coerce")
  df_rev_clean = df_rev.dropna(subset=[col_val_fact]).copy()

  col_fv = "FV" if "FV" in df_rev.columns else "Facturas"
  col_mes = "Mes" if "Mes" in df_rev.columns else "MES"

  grouped_rev = (
      df_rev_clean.groupby("RQ_CLEAN")
      .agg({
          col_val_fact: "sum",
          col_fv: lambda x: " / ".join(
              set(x.dropna().astype(str).str.strip().apply(clean_key))
          ),
          col_mes: lambda x: "/".join(
              set(x.dropna().astype(str).str.strip())
          ),
      })
      .reset_index()
  )
  grouped_rev.rename(
      columns={
          "RQ_CLEAN": "RQ",
          col_val_fact: "Valor_Total",
          col_fv: "Facturas",
          col_mes: "MesesAgrupados",
      },
      inplace=True,
  )

  map_rev = grouped_rev.set_index("RQ").to_dict(orient="index")

  # 3. Procesar Cuadro Control
  col_nit_prov = (
      "NIT PROVEEDOR"
      if "NIT PROVEEDOR" in df_cuadro.columns
      else "NIT_PROVEEDOR"
  )
  col_fac_prov = (
      "FACTURA"
      if "FACTURA" in df_cuadro.columns
      else "FACTURA PROVEEDOR"
  )
  col_req_cuadro = (
      "REQUERIMIENTO"
      if "REQUERIMIENTO" in df_cuadro.columns
      else "REQUERIMIENTO"
  )
  col_val_cliente = (
      "VALOR CLIENTE"
      if "VALOR CLIENTE" in df_cuadro.columns
      else "VALOR FACTURA CLIENTE"
  )

  df_cuadro["PROVEEDOR"] = (
      df_cuadro["PROVEEDOR"].fillna("")
      if "PROVEEDOR" in df_cuadro.columns
      else ""
  )
  df_cuadro["NIT PROVEEDOR"] = df_cuadro[col_nit_prov].apply(clean_key)
  df_cuadro["FACTURA_AJUSTADA"] = (
      df_cuadro[col_fac_prov]
      .astype(str)
      .str.replace(r"[^0-9]", "", regex=True)
      .replace("nan", "")
  )

  def concat_nit_fac(row):
    nit, fac = row["NIT PROVEEDOR"], row["FACTURA_AJUSTADA"]
    if nit and fac:
      return f"{nit}-{fac}"
    return nit if nit else fac

  df_cuadro["CONCATENADO NIT - FACTURA PROVEEDOR"] = df_cuadro.apply(
      concat_nit_fac, axis=1
  )
  df_cuadro["RQ_CLEAN"] = df_cuadro[col_req_cuadro].apply(clean_key)

  if col_val_cliente in df_cuadro.columns:
    df_cuadro[col_val_cliente] = pd.to_numeric(
        df_cuadro[col_val_cliente], errors="coerce"
    ).fillna(0)
    map_factura_cliente_val = (
        df_cuadro.groupby("CONCATENADO NIT - FACTURA PROVEEDOR")[
            col_val_cliente
        ]
        .sum()
        .to_dict()
    )
  else:
    map_factura_cliente_val = {}

  map_cuadro = dict(
      zip(df_cuadro["CONCATENADO NIT - FACTURA PROVEEDOR"], df_cuadro["RQ_CLEAN"])
  )
  conteo_cuadro = df_cuadro[
      "CONCATENADO NIT - FACTURA PROVEEDOR"
  ].value_counts().to_dict()

  # 4. Procesar Facturas Nova
  for col in [
      "Identificacion Proveedor",
      "Fecha Documento",
      "Num. Documento",
      "Tipo Documento",
      "Subtipo Documento",
      "Numero Factura",
  ]:
    if col in df_fnova.columns:
      df_fnova[col] = df_fnova[col].apply(clean_key)
    else:
      df_fnova[col] = ""

  df_fnova["Concatenado"] = (
      df_fnova["Identificacion Proveedor"]
      + df_fnova["Fecha Documento"]
      + df_fnova["Num. Documento"]
      + df_fnova["Tipo Documento"]
      + df_fnova["Subtipo Documento"]
  )

  map_fnova = dict(zip(df_fnova["Concatenado"], df_fnova["Numero Factura"]))

  # 5. Filtrar y Procesar Costos Novasoft
  col_cc = None
  for c in df_costos.columns:
    if "CENTRO" in c.upper() and "COSTO" in c.upper():
      col_cc = c
      break
  if not col_cc:
    col_cc = df_costos.columns[0]

  col_linea = None
  for c in df_costos.columns:
    if "LINEA" in c.upper():
      col_linea = c
      break
  if not col_linea:
    col_linea = (
        df_costos.columns[3]
        if len(df_costos.columns) > 3
        else df_costos.columns[0]
    )

  def clean_cc(val):
    s = str(val).split(".")[0].strip()
    return s.zfill(5) if len(s) < 5 and s.isdigit() else s

  df_costos[col_cc] = df_costos[col_cc].apply(clean_cc)
  df_costos[col_linea] = df_costos[col_linea].astype(str).str.strip()

  search_cc = [
      "01987",
      "03597",
      "03661",
      "03662",
      "1987",
      "3597",
      "3661",
      "3662",
  ]
  search_lineas = [
      "MANTENIMIENTO",
      "LIMPIEZA Y CAFETERIA",
      "SERVICIOS ESPECIALIZADOS",
  ]

  cond1 = (
      df_costos[col_cc]
      .astype(str)
      .str.contains("|".join(search_cc), case=False, na=False)
  )
  cond2 = df_costos[col_linea].str.contains(
      "|".join(search_lineas), case=False, na=False
  )

  df_costos_filtered = df_costos[cond1 & cond2].copy()
  if len(df_costos_filtered) == 0:
    df_costos_filtered = df_costos.copy()

  for col in [
      "Codigo Del Tercero - Nit",
      "Fecha",
      "Numero Docuemnto Causacion",
      "Tipo De Documento",
      "Tipo De Documento De Venta / Despacho",
  ]:
    if col in df_costos_filtered.columns:
      df_costos_filtered[col] = df_costos_filtered[col].apply(clean_key)
    else:
      df_costos_filtered[col] = ""

  df_costos_filtered["Concatenado para FV"] = (
      df_costos_filtered["Codigo Del Tercero - Nit"]
      + df_costos_filtered["Fecha"]
      + df_costos_filtered["Numero Docuemnto Causacion"]
      + df_costos_filtered["Tipo De Documento"]
      + df_costos_filtered["Tipo De Documento De Venta / Despacho"]
  )

  # 6. Procesar Facturas DIAN
  col_dian_nit = (
      "NIT Emisor" if "NIT Emisor" in df_dian.columns else df_dian.columns[0]
  )
  col_dian_folio = (
      "Folio" if "Folio" in df_dian.columns else df_dian.columns[1]
  )

  df_dian[col_dian_nit] = df_dian[col_dian_nit].apply(clean_key)
  df_dian[col_dian_folio] = df_dian[col_dian_folio].apply(clean_key)
  tot_col = "Total" if "Total" in df_dian.columns else df_dian.columns[-1]
  iva_col = "IVA" if "IVA" in df_dian.columns else df_dian.columns[-2]

  df_dian["Total"] = pd.to_numeric(df_dian[tot_col], errors="coerce").fillna(0)
  df_dian["IVA"] = pd.to_numeric(df_dian[iva_col], errors="coerce").fillna(0)
  df_dian["Valor sin IVA"] = df_dian["Total"] - df_dian["IVA"]
  df_dian["Concatenado"] = df_dian[col_dian_nit] + "-" + df_dian[col_dian_folio]
  dian_set = set(df_dian["Concatenado"].dropna())

  # 7. Cruces principales
  df_costos_filtered["FP"] = df_costos_filtered["Concatenado para FV"].map(
      map_fnova
  )

  def gen_concat_req(row):
    nit, fp = row["Codigo Del Tercero - Nit"], row["FP"]
    if nit and pd.notna(fp) and str(fp).strip() != "":
      return f"{nit}-{fp}"
    return None

  df_costos_filtered["ConcatenadoRequerimiento"] = df_costos_filtered.apply(
      gen_concat_req, axis=1
  )
  df_costos_filtered["Requerimiento"] = df_costos_filtered[
      "ConcatenadoRequerimiento"
  ].map(map_cuadro)

  col_deb = None
  for c in df_costos_filtered.columns:
    if "DEBITO" in c.upper() or "DÉBITO" in c.upper():
      col_deb = c
      break
  if not col_deb:
    col_deb = (
        "Débitos Moneda Local"
        if "Débitos Moneda Local" in df_costos_filtered.columns
        else df_costos_filtered.columns[-1]
    )

  facturas_list, valor_fact_list, utilidad_list, rentabilidad_list = (
      [],
      [],
      [],
      [],
  )

  for _, row in df_costos_filtered.iterrows():
    rq_val = (
        clean_key(row["Requerimiento"])
        if pd.notna(row["Requerimiento"])
        else ""
    )
    debito_val = row.get(col_deb, 0)
    try:
      debito_val = float(debito_val)
    except Exception:
      debito_val = 0.0

    if rq_val and rq_val in map_rev:
      fac = map_rev[rq_val]["Facturas"]
      val = map_rev[rq_val]["Valor_Total"]
      util = val - debito_val
      rent = (util / debito_val) if debito_val != 0 else 0
    else:
      fac, val, util, rent = 0, 0, 0, 0

    facturas_list.append(fac)
    valor_fact_list.append(val)
    utilidad_list.append(util)
    rentabilidad_list.append(rent)

  df_costos_filtered["FACTURA"] = facturas_list
  df_costos_filtered["VALOR FACTURA"] = valor_fact_list
  df_costos_filtered["UTILIDAD"] = utilidad_list
  df_costos_filtered["RENTABILIDAD"] = rentabilidad_list

  df_costos_filtered["Cant. RQ"] = (
      df_costos_filtered["ConcatenadoRequerimiento"]
      .map(conteo_cuadro)
      .fillna(0)
  )

  # CRUCE CON DIAN ROBUSTO
  df_costos_filtered["Cruce con DIAN"] = df_costos_filtered[
      "ConcatenadoRequerimiento"
  ].apply(
      lambda x: (
          "Cruza"
          if (pd.notna(x) and str(x).strip() != "" and x in dian_set)
          else "Alerta"
      )
  )

  # 8. Agrupación RQ para Alertas & Status OBS_2
  agrupado_status = {}
  for _, row in df_costos_filtered.iterrows():
    rq = clean_key(row["Requerimiento"])

    if not es_requerimiento_valido(rq):
      rq = "0"

    debit = float(row[col_deb]) if pd.notna(row[col_deb]) else 0
    val_fac = (
        float(row["VALOR FACTURA"]) if pd.notna(row["VALOR FACTURA"]) else 0
    )
    fac_num = clean_key(row["FACTURA"])

    if rq not in agrupado_status:
      agrupado_status[rq] = {
          "debitos": 0,
          "val_fac": 0,
          "facturaRef": "0",
          "conteo": 0,
      }

    agrupado_status[rq]["debitos"] += debit
    agrupado_status[rq]["val_fac"] += val_fac
    agrupado_status[rq]["conteo"] += 1

    if fac_num and fac_num not in ["0", "0.0"]:
      agrupado_status[rq]["facturaRef"] = fac_num

  status_map = {}
  for rq, data in agrupado_status.items():
    divisor = data["conteo"] if data["conteo"] > 0 else 1
    val_real = data["val_fac"] / divisor
    utilidad = val_real - data["debitos"]

    if rq == "0":
      status = "SIN REQUERIMIENTO"
    elif str(data["facturaRef"]) in ["0", "0.0", ""]:
      status = "SIN FACTURAR AL CLIENTE"
    elif utilidad <= 0:
      status = "A PERDIDA"
    else:
      status = "SIN NOVEDAD"

    status_map[rq] = status

  def get_obs2(row):
    rq_str = clean_key(row["Requerimiento"])

    if not es_requerimiento_valido(rq_str):
      return MAPA_ESTADOS["SIN REQUERIMIENTO"]

    fac_num = clean_key(row["FACTURA"])
    if not fac_num or fac_num in ["0", "0.0"]:
      return MAPA_ESTADOS["SIN FACTURAR AL CLIENTE"]

    obs = status_map.get(rq_str, "SIN REQUERIMIENTO")
    concat_req = row["ConcatenadoRequerimiento"]
    val_concat_cliente = map_factura_cliente_val.get(concat_req, 0)

    if obs == "SIN FACTURAR AL CLIENTE" and val_concat_cliente > 0:
      deb = float(row[col_deb]) if pd.notna(row[col_deb]) else 0
      util_concat = val_concat_cliente - deb
      estado_original = "SIN NOVEDAD" if util_concat > 0 else "A PERDIDA"
    else:
      estado_original = obs

    return MAPA_ESTADOS.get(estado_original, estado_original)

  df_costos_filtered["OBS_2"] = df_costos_filtered.apply(get_obs2, axis=1)

  os.makedirs(carpeta_salida, exist_ok=True)
  df_costos_filtered.to_excel(ruta_excel_salida, index=False)

  return df_costos_filtered


# ==========================================
# BANNER INSTITUCIONAL CON LOGO COMPLETO SVG
# ==========================================
st.markdown(
    """
    <div class="header-brand">
        <div class="header-brand-content">
            <img src="https://cdn1.totalcommerce.cloud/casalimpia/web_content/assets/logo-casa-limpia.svg" alt="Casalimpia Logo" />
            <div class="title-text">
                <h1>Auditor-IA Costos Tercerizados TigoUNE</h1>
                <p>Plataforma Corporativa para el Cruce de Costos vs. Facturado</p>
            </div>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# ==========================================
# SECCIÓN 1: CARGA DE BASES DE DATOS Y EJECUCIÓN (CON TOOLTIPS DE COMENTARIOS)
# ==========================================
st.markdown("<h2>1. 📁 Carga de Bases de Datos</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='color:#666;'>Cargue las bases requeridas para iniciar la"
    " automatización del cruce preliminar.</p>",
    unsafe_allow_html=True,
)

st.markdown('<div class="card-box">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
  f1 = st.file_uploader(
      "1. BBDD Costos Novasoft (Obligatorio)",
      type=["xlsx"],
      help=(
          "Cargue el archivo “COSTOS Y PRESUPUESTOS RAFA” generado del módulo"
          " CONTABILIDAD NIF Novasoft"
      ),
  )
  if f1:
    guardar_archivo(f1)
    st.markdown(
        '<div class="badge-success">💾 Guardado en carpeta</div>',
        unsafe_allow_html=True,
    )

with col2:
  f2 = st.file_uploader(
      "2. BBDD Reversiones (Obligatorio)",
      type=["xlsx"],
      help=(
          "Cargue el archivo unificado de las Reversiones enviadas por Tigo"
          " UNE, Únicamente las columnas RQ, Valor Facturado, EA, FV, Mes"
          " formato “Julio-2026”."
      ),
  )
  if f2:
    guardar_archivo(f2)
    st.markdown(
        '<div class="badge-success">💾 Guardado en carpeta</div>',
        unsafe_allow_html=True,
    )

with col3:
  f3 = st.file_uploader(
      "3. BBDD F-100 (Obligatorio)",
      type=["xlsx"],
      help=(
          "Cargue el archivo de la hoja F–100 G. TIGO enviado por el área de"
          " Facturación."
      ),
  )
  if f3:
    guardar_archivo(f3)
    st.markdown(
        '<div class="badge-success">💾 Guardado en carpeta</div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

col4, col5, col6 = st.columns([1, 1, 1])

with col4:
  f4 = st.file_uploader(
      "4. Cuadro-control (Obligatorio)",
      type=["xlsx"],
      help=(
          "Cargue el archivo “Cuadro Control” enviado por Tigo UNE hasta la"
          " columna PROVISIÓN."
      ),
  )
  if f4:
    guardar_archivo(f4)
    st.markdown(
        '<div class="badge-success">💾 Guardado en carpeta</div>',
        unsafe_allow_html=True,
    )

with col5:
  f5 = st.file_uploader(
      "5. Facturas Nova (Obligatorio)",
      type=["xlsx"],
      help=(
          "Cargue el archivo “Factura CXP consulta” generado desde el módulo"
          " CONTABILIDAD NIF Novasoft"
      ),
  )
  if f5:
    guardar_archivo(f5)
    st.markdown(
        '<div class="badge-success">💾 Guardado en carpeta</div>',
        unsafe_allow_html=True,
    )

with col6:
  f6 = st.file_uploader(
      "6. Facturas Dian (Obligatorio)",
      type=["xlsx"],
      help="Cargue el archivo generado por la DIAN",
  )
  if f6:
    guardar_archivo(f6)
    st.markdown(
        '<div class="badge-success">💾 Guardado en carpeta</div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
col_btn_center = st.columns([1, 2, 1])[1]

with col_btn_center:
  if st.button("🚀 Procesar Cruce", type="primary", use_container_width=True):
    if not f1 or not f2 or not f3 or not f4 or not f5 or not f6:
      st.error(
          "⚠️ Debes cargar los 6 archivos obligatorios antes de procesar el"
          " cruce."
      )
    else:
      with st.spinner("⚡ Procesando cruce de datos en Python..."):
        try:
          r1 = os.path.join(CARPETA_DESTINO, f1.name)
          r2 = os.path.join(CARPETA_DESTINO, f2.name)
          r3 = os.path.join(CARPETA_DESTINO, f3.name)
          r4 = os.path.join(CARPETA_DESTINO, f4.name)
          r5 = os.path.join(CARPETA_DESTINO, f5.name)
          r6 = os.path.join(CARPETA_DESTINO, f6.name)

          procesar_cruce_python(
              r1,
              r2,
              r4,
              r5,
              r6,
              CARPETA_DESTINO,
              RUTA_ARCHIVO_DEPURADO,
          )
          st.success("✅ Cruce de datos ejecutado con éxito.")
          st.rerun()
        except Exception as e:
          st.error(f"❌ Error al procesar los datos: {e}")

st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# SECCIÓN 2: RESULTADOS DEL CRUCE
# ==========================================
if os.path.exists(RUTA_ARCHIVO_DEPURADO):
  st.markdown("<h2>2. 📊 Resultado</h2>", unsafe_allow_html=True)

  try:
    df_depurado = pd.read_excel(RUTA_ARCHIVO_DEPURADO)

    if "OBS_2" in df_depurado.columns and len(df_depurado) > 0:
      conteos = df_depurado["OBS_2"].value_counts().to_dict()

      total_filas = len(df_depurado)
      nombre_correcta = MAPA_ESTADOS["SIN NOVEDAD"]
      nombre_sin_cobro = MAPA_ESTADOS["SIN FACTURAR AL CLIENTE"]
      nombre_perdida = MAPA_ESTADOS["A PERDIDA"]
      nombre_sin_req = MAPA_ESTADOS["SIN REQUERIMIENTO"]

      cant_correcta = conteos.get(nombre_correcta, 0)
      cant_sin_cobro = conteos.get(nombre_sin_cobro, 0)
      cant_perdida = conteos.get(nombre_perdida, 0)
      cant_sin_req = conteos.get(nombre_sin_req, 0)

      # BUSCAR COLUMNA DE DÉBITOS
      col_deb_nombre = None
      for c in df_depurado.columns:
        if "DEBITO" in c.upper() or "DÉBITO" in c.upper():
          col_deb_nombre = c
          break

      monto_debitos = (
          df_depurado[col_deb_nombre].sum()
          if col_deb_nombre and col_deb_nombre in df_depurado.columns
          else 0
      )
      monto_facturado = (
          df_depurado["VALOR FACTURA"].sum()
          if "VALOR FACTURA" in df_depurado.columns
          else 0
      )

      # CÁLCULO PRECISO Y EXATCO DE ALERTAS DIAN (Ajuste Solucionado)
      col_dian_cruce = None
      for c in df_depurado.columns:
        if "DIAN" in c.upper():
          col_dian_cruce = c
          break

      if col_dian_cruce and "Cruce con DIAN" in df_depurado.columns:
        cant_alertas_dian = (
            df_depurado["Cruce con DIAN"].astype(str).str.strip() == "Alerta"
        ).sum()
      elif col_dian_cruce:
        cant_alertas_dian = (
            df_depurado[col_dian_cruce].astype(str).str.strip() == "Alerta"
        ).sum()
      else:
        cant_alertas_dian = 0

      # CÁLCULO DE UTILIDAD GENERAL (%)
      if monto_debitos != 0:
        utilidad_general_pct = (
            (monto_facturado - monto_debitos) / monto_debitos
        ) * 100
      else:
        utilidad_general_pct = 0.0

      # BARRA DE RESUMEN EJECUTIVO
      st.markdown(
          f"""
            <div class="summary-bar">
                <div class="summary-item">
                    <div class="label">Monto Débitos Moneda Local</div>
                    <div class="value">$ {monto_debitos:,.0f} COP</div>
                </div>
                <div class="summary-item">
                    <div class="label">Monto Facturado Proveedor</div>
                    <div class="value">$ {monto_facturado:,.0f} COP</div>
                </div>
                <div class="summary-item">
                    <div class="label">Utilidad General</div>
                    <div class="value">{utilidad_general_pct:.2f}%</div>
                </div>
                <div class="summary-item">
                    <div class="label">Cant. Alertas DIAN</div>
                    <div class="value">{cant_alertas_dian:,}</div>
                </div>
            </div>
            """,
          unsafe_allow_html=True,
      )

      # CÁLCULO DE VALORES ($) ESPECÍFICOS PARA CADA TARJETA KPI
      monto_sin_cobro = (
          df_depurado[df_depurado["OBS_2"] == nombre_sin_cobro][
              col_deb_nombre
          ].sum()
          if col_deb_nombre
          else 0
      )

      monto_perdida_utilidad = (
          df_depurado[df_depurado["OBS_2"] == nombre_perdida]["UTILIDAD"].sum()
          if "UTILIDAD" in df_depurado.columns
          else 0
      )

      monto_sin_req_debit = (
          df_depurado[df_depurado["OBS_2"] == nombre_sin_req][
              col_deb_nombre
          ].sum()
          if col_deb_nombre
          else 0
      )

      st.markdown('<div class="card-box">', unsafe_allow_html=True)

      # TARJETAS DE KPI REORDENADAS
      kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

      with kpi1:
        st.markdown(
            f"""
            <div class="kpi-card-exec border-total">
                <h4>Total Filas Procesadas</h4>
                <div class="kpi-num">{total_filas:,}</div>
                <div style="visibility: hidden;" class="kpi-money">-</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

      with kpi2:
        st.markdown(
            f"""
            <div class="kpi-card-exec border-correcto">
                <h4>{nombre_correcta}</h4>
                <div class="kpi-num">{cant_correcta:,}</div>
                <div style="visibility: hidden;" class="kpi-money">-</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

      with kpi3:
        st.markdown(
            f"""
            <div class="kpi-card-exec border-nocobro">
                <h4>{nombre_sin_cobro}</h4>
                <div class="kpi-num">{cant_sin_cobro:,}</div>
                <div class="kpi-money">$ {monto_sin_cobro:,.0f} COP</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

      with kpi4:
        st.markdown(
            f"""
            <div class="kpi-card-exec border-perdida">
                <h4>{nombre_perdida}</h4>
                <div class="kpi-num">{cant_perdida:,}</div>
                <div class="kpi-money">$ {monto_perdida_utilidad:,.0f} COP</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

      with kpi5:
        st.markdown(
            f"""
            <div class="kpi-card-exec border-sinreq">
                <h4>{nombre_sin_req}</h4>
                <div class="kpi-num">{cant_sin_req:,}</div>
                <div class="kpi-money">$ {monto_sin_req_debit:,.0f} COP</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

      st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)

      # FILTROS Y BUSCADOR UNIVERSAL
      col_filtro_est, col_busqueda, col_btn_exp = st.columns([1.5, 1.5, 1])

      opciones_filtro = ["Todos los estados"] + sorted(
          list(df_depurado["OBS_2"].dropna().unique())
      )

      with col_filtro_est:
        estado_seleccionado = st.selectbox(
            "🔍 **Filtrar por Estado:**", options=opciones_filtro, index=0
        )

      with col_busqueda:
        texto_busqueda = st.text_input(
            "🔎 **Buscador en la Tabla:**",
            placeholder="Factura, NIT, Proveedor, RQ...",
        )

      if estado_seleccionado != "Todos los estados":
        df_mostrar = df_depurado[
            df_depurado["OBS_2"] == estado_seleccionado
        ].copy()
      else:
        df_mostrar = df_depurado.copy()

      if texto_busqueda.strip() != "":
        mask = df_mostrar.astype(str).apply(
            lambda row: row.str.contains(texto_busqueda, case=False, na=False)
        ).any(axis=1)
        df_mostrar = df_mostrar[mask]

      # PÍLDORAS TRANSLÚCIDAS DE COLOR
      def color_obs2(val):
        if val == MAPA_ESTADOS["SIN NOVEDAD"]:
          return "background-color: rgba(131, 180, 49, 0.25); color: #2e470c; font-weight: bold;"
        elif val == MAPA_ESTADOS["SIN FACTURAR AL CLIENTE"]:
          return "background-color: rgba(225, 29, 72, 0.25); color: #881337; font-weight: bold;"
        elif val == MAPA_ESTADOS["A PERDIDA"]:
          return "background-color: rgba(249, 115, 22, 0.25); color: #7c2d12; font-weight: bold;"
        elif val == MAPA_ESTADOS["SIN REQUERIMIENTO"]:
          return "background-color: rgba(17, 121, 191, 0.25); color: #0c4a6e; font-weight: bold;"
        return ""

      df_styled = df_mostrar.style.map(color_obs2, subset=["OBS_2"])

      st.markdown(
          f"### 📋 Detalle de Registros ({len(df_mostrar):,} filas"
          " mostradas)"
      )
      st.dataframe(df_styled, use_container_width=True, height=450)

      # EXPORTAR RESPETANDO FILTRO Y BÚSQUEDA
      with col_btn_exp:
        st.write("##")
        buffer_excel = io.BytesIO()
        with pd.ExcelWriter(buffer_excel, engine="openpyxl") as writer:
          df_mostrar.to_excel(writer, index=False, sheet_name="Resultados")
        buffer_excel.seek(0)

        st.download_button(
            label="📥 Exportar resultados",
            data=buffer_excel,
            file_name=(
                f"Resultados_Auditoria_{estado_seleccionado.replace(' ', '_')}.xlsx"
            ),
            mime=(
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            ),
            type="primary",
            use_container_width=True,
          )

      st.markdown("</div>", unsafe_allow_html=True)
    else:
      st.warning(
          "El archivo depurado se generó pero no contiene registros para"
          " mostrar."
      )
  except Exception as e:
    st.warning(f"Cargando vista previa... ({e})")
