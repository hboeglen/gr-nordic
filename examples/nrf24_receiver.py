#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Nrf24 Receiver
# GNU Radio version: 3.10.4.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import nordic
from gnuradio import uhd
import time
import numpy



from gnuradio import qtgui

class nrf24_receiver(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Nrf24 Receiver", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Nrf24 Receiver")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "nrf24_receiver")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 2e6
        self.samp_rate = samp_rate = 4e6

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_source_0.set_center_freq(2520000000, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0.set_bandwidth(2e6, 0)
        self.uhd_usrp_source_0.set_gain(60, 0)
        self.qtgui_time_sink_x_2_0_0 = qtgui.time_sink_f(
            256, #size
            samp_rate/(samp_rate/symbol_rate), #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_2_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2_0_0.enable_tags(True)
        self.qtgui_time_sink_x_2_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.5, 0, 0, "squelch_sob")
        self.qtgui_time_sink_x_2_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_2_0_0.enable_grid(False)
        self.qtgui_time_sink_x_2_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_2_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_2_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_2_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_0_0_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "squelch_sob")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.nordic_nordictap_printer_0 = nordic.nordictap_printer()
        self.nordic_nordic_rx_0 = nordic.nordic_rx(120, 5, 2, 2)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                1.2e6,
                250e3,
                window.WIN_HAMMING,
                6.76))
        self.digital_gfsk_demod_1 = digital.gfsk_demod(
            samples_per_symbol=(int(samp_rate/symbol_rate)),
            sensitivity=(1.5707/(samp_rate/symbol_rate)),
            gain_mu=0.175,
            mu=0.5,
            omega_relative_limit=0.005,
            freq_error=0.0,
            verbose=False,
            log=False)
        self.blocks_char_to_float_2 = blocks.char_to_float(1, 1)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc((-40), (5e-4), 0, False)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.nordic_nordic_rx_0, 'nordictap_out'), (self.nordic_nordictap_printer_0, 'nordictap_in'))
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_char_to_float_2, 0), (self.qtgui_time_sink_x_2_0_0, 0))
        self.connect((self.digital_gfsk_demod_1, 0), (self.blocks_char_to_float_2, 0))
        self.connect((self.digital_gfsk_demod_1, 0), (self.nordic_nordic_rx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_gfsk_demod_1, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.analog_pwr_squelch_xx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "nrf24_receiver")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.qtgui_time_sink_x_2_0_0.set_samp_rate(self.samp_rate/(self.samp_rate/self.symbol_rate))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 1.2e6, 250e3, window.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2_0_0.set_samp_rate(self.samp_rate/(self.samp_rate/self.symbol_rate))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)




def main(top_block_cls=nrf24_receiver, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print("Error: failed to enable real-time scheduling.")

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
