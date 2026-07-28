from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from datetime import datetime

from database.tracks import tracks
from ui.track_toolbar import TrackToolBar
from ui.add_track_dialog import AddTrackDialog


class TrackLibrary(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            background:#1B1F24;
            color:white;
        """)

        layout = QVBoxLayout(self)

        title = QLabel("🎵 Track Library")
        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
            color:white;
            padding:10px;
        """)

        layout.addWidget(title)

        self.toolbar = TrackToolBar()
        layout.addWidget(self.toolbar)

        self.table = QTableWidget()

        self.table.setColumnCount(7)

        self.table.setHorizontalHeaderLabels([
            "ID",
            "Title",
            "Album",
            "Genre",
            "Mood",
            "BPM",
            "Status"
        ])

        self.table.verticalHeader().setVisible(False)

        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.table.setAlternatingRowColors(True)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout.addWidget(self.table)

        self.toolbar.refreshButton.clicked.connect(self.load_tracks)
        self.toolbar.addButton.clicked.connect(self.add_track)

        self.load_tracks()

    def load_tracks(self):

        self.table.setRowCount(0)

        data = tracks.get_tracks()

        for row, track in enumerate(data):

            self.table.insertRow(row)

            self.table.setItem(row,0,QTableWidgetItem(str(track[0])))
            self.table.setItem(row,1,QTableWidgetItem(track[1]))
            self.table.setItem(row,2,QTableWidgetItem(track[2]))
            self.table.setItem(row,3,QTableWidgetItem(track[3]))
            self.table.setItem(row,4,QTableWidgetItem(track[4]))
            self.table.setItem(row,5,QTableWidgetItem(str(track[5])))
            self.table.setItem(row,6,QTableWidgetItem(track[12]))

    def add_track(self):

        dialog = AddTrackDialog()

        if dialog.exec():

            tracks.add_track(
                dialog.titleEdit.text(),
                dialog.albumEdit.text(),
                dialog.genreEdit.text(),
                dialog.moodEdit.text(),
                dialog.bpmEdit.value(),
                dialog.keyEdit.text(),
                dialog.promptEdit.toPlainText(),
                "",
                "",
                "",
                datetime.now().strftime("%Y-%m-%d"),
                "New"
            )

            self.load_tracks()