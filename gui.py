
import sys
import os
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QFileDialog, QLabel,
    QMessageBox, QProgressBar, QTextEdit
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from main import run_analysis


class ForensicApp(QWidget):
    def __init__(self):
        super().__init__()
        self.file_path = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Forensic Tracer")
        self.setGeometry(100, 100, 600, 600)
        self.setWindowIcon(QIcon("html/icon.png"))

        layout = QVBoxLayout()

        self.label = QLabel("Выберите файл для анализа")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.choose_btn = QPushButton("📁 Выбрать файл")
        self.choose_btn.clicked.connect(self.choose_file)
        layout.addWidget(self.choose_btn)

        self.analyze_btn = QPushButton("🔍 Анализировать")
        self.analyze_btn.clicked.connect(self.analyze_file)
        self.analyze_btn.setEnabled(False)
        layout.addWidget(self.analyze_btn)

        self.progress = QProgressBar()
        self.progress.setRange(0, 0)
        self.progress.setVisible(False)
        layout.addWidget(self.progress)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.html_btn = QPushButton("🌐 Открыть HTML-отчёт")
        self.html_btn.clicked.connect(self.open_html_report)
        layout.addWidget(self.html_btn)

        self.setLayout(layout)

    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл")
        if file_path:
            self.file_path = file_path
            self.label.setText(f"Файл выбран: {os.path.basename(file_path)}")
            self.analyze_btn.setEnabled(True)

    def analyze_file(self):
        if not self.file_path:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите файл")
            return

        self.progress.setVisible(True)
        self.output.clear()
        QApplication.processEvents()

        try:
            results = run_analysis(self.file_path)
            self.display_results(results)
            QMessageBox.information(self, "Анализ завершён", "Анализ успешно выполнен. Вы можете открыть HTML-отчёт.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка анализа", str(e))
        finally:
            self.progress.setVisible(False)

    def display_results(self, results):
        output_text = ""
        for section, content in results.items():
            output_text += f"=== {section.upper()} ===\n"
            if isinstance(content, dict):
                for k, v in content.items():
                    output_text += f"{k}: {v}\n"
            elif isinstance(content, list):
                for item in content:
                    output_text += f"- {item}\n"
            else:
                output_text += str(content) + "\n"
            output_text += "\n"
        self.output.setPlainText(output_text)

    def open_html_report(self):
        report_path = os.path.abspath("html/report.html")
        if os.path.exists(report_path):
            reply = QMessageBox.question(self, "Открыть HTML отчёт", "Вы действительно хотите открыть отчёт в браузере?",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                webbrowser.open(f"file://{report_path}")
        else:
            QMessageBox.warning(self, "Файл не найден", "HTML-отчёт ещё не был сгенерирован.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ForensicApp()
    window.show()
    sys.exit(app.exec_())
