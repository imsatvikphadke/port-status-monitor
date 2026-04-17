from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3


class PortStatusMonitor(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(PortStatusMonitor, self).__init__(*args, **kwargs)
        self.logger.info("Port Status Monitor Started")

    @set_ev_cls(ofp_event.EventOFPPortStatus, MAIN_DISPATCHER)
    def port_status_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto

        reason = msg.reason
        port_no = msg.desc.port_no

        if reason == ofproto.OFPPR_ADD:
            self.logger.info("Port %s added", port_no)

        elif reason == ofproto.OFPPR_DELETE:
            self.logger.info("Port %s deleted", port_no)

        elif reason == ofproto.OFPPR_MODIFY:
            if msg.desc.state == 0:
                self.logger.info("Port %s is UP", port_no)
            else:
                self.logger.info("Port %s is DOWN", port_no)

        else:
            self.logger.info("Unknown event on port %s", port_no)
