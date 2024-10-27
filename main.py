from telethon.sync import TelegramClient

# Replace with your own API_ID and API_HASH from my.telegram.org
API_ID = 'your_api_id'
API_HASH = 'your_api_hash'

# List of session file names
sessions = ['session1', 'session2', 'session3']  # Add your session files

# New profile name you want to set
new_first_name = 'NewFirstName'
new_last_name = 'NewLastName'

for session in sessions:
    # Connect to each Telegram session
    client = TelegramClient(session, API_ID, API_HASH)
    
    async def change_name():
        await client.start()
        me = await client.get_me()
        
        # Update the profile name
        await client(functions.account.UpdateProfileRequest(
            first_name=new_first_name,
            last_name=new_last_name
        ))
        print(f'Name changed for {me.username}')
        
        await client.disconnect()

    # Run the async function
    with client:
        client.loop.run_until_complete(change_name())
