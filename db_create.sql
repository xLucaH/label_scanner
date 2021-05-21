

DROP DATABASE IF EXISTS labels_db;
CREATE DATABASE IF NOT EXISTS labels_db;

USE labels_db;

CREATE TABLE lbl_labels (
	lbl_guid VARCHAR(52),
    lbl_name VARCHAR(60),
    lbl_short_description VARCHAR(255),
    lbl_details text,
	lbl_score_total DECIMAL(4, 1),
    lbl_score_transparency DECIMAL(4, 1),
    lbl_score_ecological DECIMAL(4, 1),
    lbl_score_quality DECIMAL(4, 1),
    lbl_image_media_path VARCHAR(255),

    CONSTRAINT lbl_labels PRIMARY KEY (lbl_guid)
);

INSERT INTO lbl_labels
VALUES
('20210519124314073d39cb65-85d8-4adc-9346-087fafa0f4b8' , 'EU-Bio-Logo', 'Since july 2010, all bio products that are produced within the EU borders, are marked with this label.The label secures the "European Organic Regulation" standards.', 'Since july 2010, all bio products that are produced within the EU borders, are marked with this label.The label secures the "European Organic Regulation" standards.', 73.3, 80.0, 70.0, 70.0, 'label_images/20210519124314073d39cb65-85d8-4adc-9346-087fafa0f4b8.png'),
('202105191305397118cc7134-31fb-4de4-8f61-75b736d636bb' , 'PRO WEIDELAND', 'The "PRO WEIDELAND" label is a voluntary usable label that controls the animal standards of milk product. Every Cows must have a minimun area of 2.000 square meter with at least 1.000 square meter of green space. ', 'The "PRO WEIDELAND" label is a voluntary usable label that controls the animal standards of milk product. Every Cows must have a minimun area of 2.000 square meter with at least 1.000 square meter of green space. They should roam freely the whole year.', 83.3, 95, 65, 90, 'label_images/202105191305397118cc7134-31fb-4de4-8f61-75b736d636bb.png'),
('20210520131047636384824a-ca59-431c-8681-28961f2b0df5' , 'Fairtrade', 'The Fairtrade label is divided in three main categories: social, ecological and economical. It ensures that farmers and workers are working under social standards.','The Fairtrade label is divided in three main categories: social, ecological and economical. It ensures that farmers and workers are working under social standards.The most metionable standards include: No work for children under the age of 15, no discrimination and minimum prices for certain products', 62, 55, 65, 65, 'label_images/20210520131047636384824a-ca59-431c-8681-28961f2b0df5.png'),
('20210521063012572b3c6070-3882-4d29-9004-4286eaf8bdf8', 'Neuland', 'The \"Neuland\" label is focused on providing an animal and ecological friendly husbandry of the animals.Neuland is not a bio label but rather a program for especially high animal husbandry standards.', 'The \"Neuland\" label is focused on providing an animal and ecological friendly husbandry of the animals.Neuland is not a bio label but rather a program for especially high animal husbandry standards.\nMost important standards:\nNo fixation of the animals\nAbility for the animal to spend the whole day outside\nOnly food for the animals that comes from the region.', '80.0', '90.0', '70.0', '80.0', 'label_images/20210521063012572b3c6070-3882-4d29-9004-4286eaf8bdf8.png');
