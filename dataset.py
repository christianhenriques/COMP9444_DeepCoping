import zipfile, json, os

zip_path = "dataset.zip"        # downloaded from the UMN Conservancy page
out_dir = "trashcan"

with zipfile.ZipFile(zip_path) as z:
    z.extractall(out_dir)

# Check the actual folder layout and JSON file names after extraction
for root, dirs, files in os.walk(out_dir):
    depth = root.count(os.sep) - out_dir.count(os.sep)
    if depth < 3:
        print(root, [f for f in files if f.endswith(".json")])
      
# pip install pycocotools
from pycocotools.coco import COCO

# Adjust these paths to match what the listing above printed
ann_file = "trashcan/dataset/instance_version/instances_train_trashcan.json"   # or material_version/...
coco = COCO(ann_file)

cats = coco.loadCats(coco.getCatIds())
print([c["name"] for c in cats])

img_id = coco.getImgIds()[0]
img_info = coco.loadImgs(img_id)[0]
anns = coco.loadAnns(coco.getAnnIds(imgIds=img_id))
print(img_info["file_name"], len(anns))
for a in anns:
    print(a["category_id"], a["bbox"])   # bbox = [x, y, w, h]; a["segmentation"] holds the mask
