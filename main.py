from fastapi import FastAPI
from routers import cierre_diario, saldo, tenencia_valorizada, add_saldo, compra, venta, reset_wallet

app = FastAPI()

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

