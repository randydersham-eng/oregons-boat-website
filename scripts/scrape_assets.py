import urllib.request
import os

def download_file(url, local_path):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    try:
        print(f"Downloading {url} to {local_path}...")
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())
        print("Success.")
    except Exception as e:
        print(f"Failed: {e}")

def main():
    assets_dir = "/Users/randydersham/Desktop/VIBE CODE PROJECTS/OREGON'S BOAT WEBSITE/assets"
    os.makedirs(assets_dir, exist_ok=True)
    
    assets = {
        "Oregon_Boat_Title.png": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/84e42e90-3045-4b3e-9756-89f775a001d2/Oregon%27s-Boat-Title-1.png?format=1500w",
        "shutterstock_boat.jpg": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/0de6b28e-88b2-4453-a185-09fff86d2b90/shutterstock_1201142464-web.jpg",
        "Prince_Helfrich_trip.jpg": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/2f188d6c-73a4-4c9d-b5ae-e282a79230ca/Prince+Helfrich+trip_for_web.jpg",
        "laurel_best_shorts.png": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/071ade54-5897-4f1f-8ec4-967ff8109309/BEST-SHORTS-Merit-SM-logo-White-768x407.png",
        "laurel_winner_best_short.png": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/d6952648-74d1-446d-80f5-5ec8f0780fe1/Winner-Best-Short-Film.png",
        "laurel_odff_winner.png": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/a1638380-63c5-4faf-bc8e-ee4d3d783aa4/ODFF-Winter-2025-WINNER-Laurel-White.png",
        "laurel_lwff_honorable.png": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/8aa6152f-9aa7-4bd6-b1ef-166665274fa8/lwff_2025_laurels_honorable_mentionn_white.png",
        "laurel_east_village.png": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/ae61478e-75b8-443e-ba6e-5b46a4719266/East_Village_New_York_Film_Festival_-_BEST_FIRST_TIME_DIRECTOR__-_.png",
        "laurel_oregon_coast.png": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/ab1421da-78b3-43b2-a4d9-ba496709540f/CLOSINGFILM-OregonCoastFilmFestival-2025-%281%29.png",
        "laurel_indiefest.png": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/341e312b-b5f4-466f-b686-6b868cc0620f/IndieFEST-Merit-Words-white-outline.png",
        "laurel_nature_borders.png": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/6b6c2cc3-8cf9-408a-9fce-f2446c682d15/BESTOFSHOW-NatureWithoutBordersInternationalFilmFestival-white.png",
        "favicon.png": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/c7664d2d-4234-490d-8edf-e659e692ebf1/Oregon%27s-Boat-favicon.png",
        "McKenzie_Driftboat_Festival.jpg": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/60dbd71a-c4cb-4c6b-aa62-bb939dc3b94e/McKenzie-Driftboat-Festival.jpg",
        "laurel_odff_winner_color.jpg": "https://images.squarespace-cdn.com/content/v1/6100c4131073a339a72b7b4f/2cbdfade-dfd0-4951-892c-22a1039d8f81/ODFF-Winter-2025-WINNER-Laurel.jpg"
    }

    for filename, url in assets.items():
        local_path = os.path.join(assets_dir, filename)
        download_file(url, local_path)

if __name__ == "__main__":
    main()
