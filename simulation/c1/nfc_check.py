import asyncio
import nfc

async def detect_nfc_tags():
    def on_connect(tag):
        # Process the detected NFC tag here
        print("NFC Tag detected:", tag)

    clf = nfc.ContactlessFrontend()
    while True:
        await clf.connect(rdwr={'on-connect': on_connect})

async def main():
    # Your main code here
    while True:
        print("Main code running...")
        await asyncio.sleep(1)  # Simulate some work

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    nfc_task = loop.create_task(detect_nfc_tags())
    main_task = loop.create_task(main())

    try:
        loop.run_until_complete(asyncio.gather(nfc_task, main_task))
    except KeyboardInterrupt:
        # Handle keyboard interrupt (e.g., Ctrl+C)
        nfc_task.cancel()
        main_task.cancel()
        loop.run_until_complete(asyncio.gather(nfc_task, main_task))
    finally:
        loop.close()