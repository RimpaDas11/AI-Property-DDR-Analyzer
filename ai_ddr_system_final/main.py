from modules.pdf_extractor import extract_text
from modules.image_extractor import extract_images
from modules.text_processor import extract_observations
from modules.data_merger import merge_data
from modules.ddr_generator import generate_ddr
import config

def main():
    inspection_text = extract_text(config.INPUT_INSPECTION)
    thermal_text = extract_text(config.INPUT_THERMAL)

    inspection_images = extract_images(config.INPUT_INSPECTION, config.IMAGE_OUTPUT_DIR)
    thermal_images = extract_images(config.INPUT_THERMAL, config.IMAGE_OUTPUT_DIR)

    obs1 = extract_observations(inspection_text)
    obs2 = extract_observations(thermal_text)

    merged_data = merge_data(obs1, obs2)
    all_images = inspection_images + thermal_images

    generate_ddr(merged_data, all_images, config.OUTPUT_REPORT)
    print("DDR Report Generated Successfully!")

if __name__ == "__main__":
    main()
