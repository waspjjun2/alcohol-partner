import logging

from alcoholpartner.bot import AlcoholPartner

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

TOKEN = '<TOKEN_HERE>'

partner = AlcoholPartner(token=TOKEN)
partner.start()
