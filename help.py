import hikari

bot = hikari.GatewayBot(token="OTQ4NjIzODUwNzE3OTgyNzIx.Yh-gzg.vNpr_4dX5ZEPT2hmkqKXq5UPbWs")

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    # If a non-bot user sends a message "hk.ping", respond with "Pong!"
    # We check there is actually content first, if no message content exists,
    # we would get `None' here.
    if event.is_bot or not event.content:
        return

    if event.content.startswith(".ping"):
        await event.message.respond("Pong!")

bot.run()
