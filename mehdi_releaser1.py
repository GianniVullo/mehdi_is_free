import pdfplumber

total_width = 3507
total_height = 2479


def height_ratio(coord):
    return coord/total_height


def width_ratio(coord):
    return coord/total_width


def coord(x0, top, x1, bottom):
    return (width_ratio(x0) * 841.890, height_ratio(top) * 595.280, width_ratio(x1) * 841.890, height_ratio(bottom) * 595.280)

def extractor(page, x0, top, x1, bottom):
    return pdf.pages[page].within_bbox(
        coord(x0, top, x1, bottom),
        relative=False).extract_text(x_tolerance=3, y_tolerance=3)

with pdfplumber.open('property-477.pdf') as pdf:
    adresse = extractor(0, 135, 1957, 1596, 2273)
    postcode = extractor(0, 1703, 1963, 2333, 2090)
    description = extractor(0, 148, 2441, 2330, 3054)
    estimated_rental_per_month = extractor(2, 135, 401, 1248, 528)
    gross_yield = extractor(2,)
    asking_price = extractor(2,)
    fair_market_value = extractor(2,)
    refurb = extractor(2,)
    buying_costs = extractor(2,)
    property_type = extractor(2,)
    no_of_existing_bedrooms = extractor(2,)
    total_no_of_bedrooms_after_refurb = extractor(2,)
    reception_rooms = extractor(2,)
    bathrooms_shower_rooms = extractor(2,)
    nearest_train_station = extractor(2,)
    key_journey_time = extractor(2,)
    with open('mehdi_is_free.txt', 'a') as f:
        fields = [adresse + '\n', postcode + '\n', description + '\n', estimated_rental_per_month + '\n']
        for item in fields:
            f.write(item)
