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
          summary="Welcome",
          tags=["Welcome"])

async def welcome():
    html_content = """
    <html>
        <head>
            <title>FastAPI Root Endpoint</title>
            <style>
                h1, p {
                    text-align: center;
                }
                
                .link-container {
                    text-align: center;
                }
            </style>
        </head>
        <body background= "https://i0.wp.com/www.quebakan.com/v15/wp-content/uploads/2022/09/app-peigo.jpg?resize=700%2C904&ssl=1" bgcolor="FFCECB">
            <h1>Cripto Exchange</h1>
            <p>Una nueva forma de administrar tu dinero</p>            
            <p>Para acceder a la documentación de la API, visite:</p>
            <div class="link-container">
                <a href="https://exchange-nfmb.onrender.com/docs">Documentación de la API</a>
            </div>
        </body>
    </html>
    """
    return html_content

# @app.get("/")
# async def welcome():
#     html_content = FileResponse("wallet.jpg")
#     return html_content

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

