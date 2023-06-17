import json

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTableWidget, QHeaderView, QTableWidgetItem, QHBoxLayout, \
    QPushButton

from upload_images import uploadImages, uploadSealDetails


class AddSightingsDialog(QDialog):
    sightings: list

    def __init__(self,  date, location, server_url):
        super().__init__()
        self.sightings = []
        self.setWindowTitle("Add Sightings")
        self.resize(800, 800)
        layout = QVBoxLayout()

        self.add_sightings_table = QTableWidget()
        header_labels = ["Name", "Comments", "With Pup", "Age", "Gender",  "Image"]
        self.add_sightings_table.setColumnCount(len(header_labels))
        self.add_sightings_table.setHorizontalHeaderLabels(header_labels)
        self.add_sightings_table.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.AnyKeyPressed)
        self.add_sightings_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Initialize the table with 10 rows
        self.add_sightings_table.setRowCount(10)
        for row in range(self.add_sightings_table.rowCount()):
            for col in range(self.add_sightings_table.columnCount()):
                item = QTableWidgetItem()
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self.add_sightings_table.setItem(row, col, item)

        layout.addWidget(self.add_sightings_table)

        button_layout = QHBoxLayout()
        add_rows_button = QPushButton("Add Rows")
        add_rows_button.clicked.connect(self.addRows)
        button_layout.addWidget(add_rows_button)

        upload_images_button = QPushButton("Upload Images")
        upload_images_button.clicked.connect(lambda: self.uploadAndAddImages(server_url, date, location))
        button_layout.addWidget(upload_images_button)

        done_button = QPushButton("Done")
        done_button.clicked.connect(lambda: self.addSightings(date, location))
        button_layout.addWidget(done_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.exec_()

    def addRows(self):
        current_row_count = self.add_sightings_table.rowCount()
        new_row_count = current_row_count + 10
        self.add_sightings_table.setRowCount(new_row_count)
        for row in range(current_row_count, new_row_count):
            for col in range(self.add_sightings_table.columnCount()):
                item = QTableWidgetItem()
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self.add_sightings_table.setItem(row, col, item)

    def uploadAndAddImages(self, server_url, date, location):
        sightings_with_images = uploadImages(server_url)
        for sighting in sightings_with_images:
            # add it to  the table
            sighting['date'] = date
            sighting['location'] = location
            self.sightings.append(sighting)
            rowcount = -1
            # find the first empty row
            for row in range(self.add_sightings_table.rowCount()):
                if self.add_sightings_table.item(row, 0).text() == '':
                    rowcount = row
                    break
            # if no empty row was found, add a new row
            if rowcount == -1:
                row_count = self.add_sightings_table.rowCount()
                self.add_sightings_table.setRowCount(row_count + 1)
            self.add_sightings_table.setItem(row_count, 0, QTableWidgetItem(sighting["id"]))
            self.add_sightings_table.setItem(row_count, 1, QTableWidgetItem(sighting["comments"]))
            self.add_sightings_table.setItem(row_count, 2, QTableWidgetItem(sighting["with_pup"]))
            self.add_sightings_table.setItem(row_count, 3, QTableWidgetItem(sighting["age"]))
            self.add_sightings_table.setItem(row_count, 4, QTableWidgetItem(sighting["gender"]))
            self.add_sightings_table.setItem(row_count, 5, QTableWidgetItem(sighting["image"]))

    def addSightings(self, date, location):
        for row in range(self.add_sightings_table.rowCount()):
            name_item = self.add_sightings_table.item(row, 0)
            comments_item = self.add_sightings_table.item(row, 1)
            with_pup_item = self.add_sightings_table.item(row, 2)
            age_item = self.add_sightings_table.item(row, 3)
            gender_item = self.add_sightings_table.item(row, 4)
            image_item = self.add_sightings_table.item(row, 5)

            name = name_item.text() if name_item else ""
            if name == '':
                continue
            comments = comments_item.text() if comments_item else ""
            with_pup = with_pup_item.text() if with_pup_item else ""
            age = age_item.text() if age_item else ""
            gender = gender_item.text() if gender_item else ""
            image = 'yes' if image_item else "no"

            sighting_details = {
                "orig_ID": name,
                'id': name,
                "comments": comments,
                "with_pup": with_pup,
                "age": age,
                "gender": gender,
                "date": date,
                'location': location,
                'Image': image,
                'viewpoint': '',
                'aid': ''
            }

            self.sightings.append(sighting_details)

        print(self.sightings)

        with open('sightings.json') as f:
            sightings_list = json.load(f)

        sightings_list.extend(self.sightings)

        # with open('sightings.json', 'w') as f:
        #     json.dump(sightings_list, f, indent=4, separators=(',', ': '))

        # for sighting in self.sightings:
        #     if sighting['image'] == 'yes':
        #         uploadSealDetails()

        print(f'Successfully added {len(self.sightings)} sightings to sightings.json')

        self.close()