import threading
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time 


async def run_file1(file_path):
    process = await asyncio.create_subprocess_exec('python', file_path, stdout=asyncio.subprocess.PIPE)
    output, _ = await process.communicate()
    return output.decode().strip()

async def main1():
    file_path =  'C:\\Users\\fibou\\Desktop\\Dossier\\comparateur_live\\macth odd.py'
    output = await run_file1(file_path)
    print(output)


import asyncio

async def run_file2(file_path):
    process = await asyncio.create_subprocess_exec('python', file_path, stdout=asyncio.subprocess.PIPE)
    output, _ = await process.communicate()
    return output.decode().strip()

async def main2():
    file_path = 'C:\\Users\\fibou\\Desktop\\Dossier\\comparateur_live\\over_under.py'
    output = await run_file2(file_path)
    print(output)



async def run_file3(file_path):
    process = await asyncio.create_subprocess_exec('python', file_path, stdout=asyncio.subprocess.PIPE)
    output, _ = await process.communicate()
    return output.decode().strip()

async def main3():
    file_path = 'C:\\Users\\fibou\\Desktop\\Dossier\\comparateur_live\\half.py'
    output = await run_file3(file_path)
    print(output)


async def run_file4(file_path):
    process = await asyncio.create_subprocess_exec('python', file_path, stdout=asyncio.subprocess.PIPE)
    output, _ = await process.communicate()
    return output.decode().strip()

async def main4():
    file_path = 'C:\\Users\\fibou\\Desktop\\Dossier\\comparateur_live\\half_0.5_goal.py'
    output = await run_file4(file_path)
    print(output)



async def run_file5(file_path):
    process = await asyncio.create_subprocess_exec('python', file_path, stdout=asyncio.subprocess.PIPE)
    output, _ = await process.communicate()
    return output.decode().strip()

async def main5():
    file_path = 'C:\\Users\\fibou\\Desktop\\Dossier\\comparateur_live\\half_1.5_goal.py'
    output = await run_file5(file_path)
    print(output)

async def run_file6(file_path):
    process = await asyncio.create_subprocess_exec('python', file_path, stdout=asyncio.subprocess.PIPE)
    output, _ = await process.communicate()
    return output.decode().strip()

async def main6():
    file_path = 'C:\\Users\\fibou\\Desktop\\Dossier\\comparateur_live\\half_2.5_goal.py'
    output = await run_file6(file_path)
    print(output)




async def main():
    # Créez un planificateur asyncio
    scheduler = AsyncIOScheduler()

    # Planifiez l'exécution des fonctions avec un intervalle spécifique (par exemple, toutes les 5 secondes)
    scheduler.add_job(main1, 'interval', seconds=25, max_instances=30)
    scheduler.add_job(main2, 'interval', seconds=25, max_instances=30)
    scheduler.add_job(main3, 'interval', seconds=25, max_instances=30)
    scheduler.add_job(main4, 'interval', seconds=25, max_instances=30)
    scheduler.add_job(main5, 'interval', seconds=25, max_instances=30)
    scheduler.add_job(main6, 'interval', seconds=25, max_instances=30)


    # Démarrez le planificateur asyncio
    scheduler.start()

    try:
        # Exécutez la boucle en continu
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        # Arrêtez le planificateur asyncio
        scheduler.shutdown()

asyncio.run(main())
client.close()