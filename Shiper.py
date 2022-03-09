from .. import loader
import random

class ShipMod(loader.Module):
	strings = {"name": "Shiper"}
	
	async def shipcmd(self, message):
		user1 = random.choice([i for i in await message.client.get_participants(message.to_id)])
		user2 = random.choice([i for i in await message.client.get_participants(message.to_id)])
		name1 = str(user1.first_name)
		name2 = str(user2.first_name)
		rand1 = message.edit(f"<a href=tg://user?id={user1.id}>{user1.first_name}</a> и <a href=tg://user?id={user2.id}>{user2.first_name}</a> любите друг друга!\nМур-Мур😻")
		rand2 = message.edit(f"<a href=tg://user?id={user1.id}>{user1.first_name}</a> и <a href=tg://user?id={user2.id}>{user2.first_name}</a> любовная парочка!\nЧмок😘")
		rand3 = message.edit(f"Пара дня❤️:\n<a href=tg://user?id={user1.id}>{user1.first_name}</a> и <a href=tg://user?id={user2.id}>{user2.first_name}</a>")
		rand4 = message.edit(f"<a href=tg://user?id={user1.id}>{user1.first_name}</a> любит <a href=tg://user?id={user2.id}>{user2.first_name}</a> 😘")
		rand5 = message.edit(f"<a href=tg://user?id={user1.id}>{user1.first_name}</a> пригласил на чай <a href=tg://user?id={user2.id}>{user2.first_name}</a> ☕❤️")
		rand6 = message.edit(f"<a href=tg://user?id={user1.id}>{user1.first_name}</a> зашел к <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n😏🔥")
		rand = [rand1, rand2, rand3, rand4, rand5, rand6]
		randchoice = random.choice(rand)
		await randchoice
