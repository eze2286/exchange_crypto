from fastapi import FastAPI

from fastapi.responses import HTMLResponse
from routers import cierre_diario, saldo, tenencia_valorizada, add_saldo, compra, venta, reset_wallet

app = FastAPI(title="Exchange Cripto",
              description="""Billetera cripto que almacena una criptomoneda y
                permite hacer diferentes operaciones como cargar saldo,
                consultarlo, comprar y vender la cripto y resetear""",
              version=1.0)

# Welcome
@app.get("/",
          response_class=HTMLResponse,          
          summary="Bienvenid@s",
          tags=["Bienvenid@s"])

async def welcome():
    html_content = """
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>FastAPI Root Endpoint</title>
            <style>
                h1, p {
                    text-align: center;
                  	margin-right: 40px;
                    font-size: 44px;                  	
                  	font-weight: bold;
                }
                
                .link-container {
                    text-align: center;
                    font-size: 25px;
                  	font-weight: bold;
                    color: blue;
                }
            </style>
        </head>
        <body background= "https://img.freepik.com/vector-gratis/moneda-virtual-bitcoin-billetera-billetes_24877-56101.jpg?w=826&t=st=1682738839~exp=1682739439~hmac=dbc21f8796d939bb963b2dedfbb9e156345f04ddcb69cc16a30cec05778a913d" bgcolor="FFCECB">
            <h1>Cripto Exchange</h1>
            <p style="font-size: 20px;">Una nueva forma de administrar tu dinero de forma segura</p>            
            <p style="font-size: 20px;">Para acceder a la documentación de la API, visite:</p>
            <div class="link-container">
                <a href="https://exchange-nfmb.onrender.com/docs" style="font-size: 20px;">Documentación de la API</a>
            </div>
        </body>
    </html>
    """
    return html_content

#ROUTERS --> se encuentran en el modulo /routers
###########################
app.include_router(cierre_diario.router)
###########################
app.include_router(saldo.router)
###########################
app.include_router(tenencia_valorizada.router)
###########################
app.include_router(add_saldo.router)
###########################
app.include_router(compra.router)
##################################
app.include_router(venta.router)
####################################
app.include_router(reset_wallet.router)
####################################

