# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service
from ncs.dp import Action
from textfsm import clitable


# ---------------
# ACTIONS EXAMPLE
# ---------------
class Show(Action):

    @Action.action
    def cb_action(self, uinfo, name, kp, input, output, trans):
        self.log.info('start show action')
        with ncs.maapi.Maapi() as m:
            with ncs.maapi.Session(m, uinfo.username, uinfo.context):
                with m.start_write_trans() as t:
                    try:
                        root = ncs.maagic.get_root(t)
                        device = root.devices.device[input.device_name]
                        
                        if "show " in input.command:
                            new_command = input.command.replace("show ","")
                        elif "sh " in input.command:
                            new_command = input.command.replace("sh ","")
                        else:
                            new_command = input.command

                        if not len(device.device_type.cli.ned_id) == 0:
                            if '-iosxr-' in device.device_type.cli.ned_id:
                                input1 = device.live_status.cisco_ios_xr_stats__exec.show.get_input()
                                input1.args = [new_command]
                                show_output = device.live_status.cisco_ios_xr_stats__exec.show(input1).result
                            elif '-ios-' in device.device_type.cli.ned_id:
                                input1 = device.live_status.ios_stats__exec.show.get_input()
                                input1.args = [new_command]
                                show_output = device.live_status.ios_stats__exec.show(input1).result
                            else:
                                show_output = "Device not supported for show command"

                        if new_command == "ip route":
                            cli_table = clitable.CliTable('index', '/home/cisco/ncs-run/templates')
                            attributes = {'Command': 'show ip route' , 'Vendor': 'Cisco'}
                            cli_table.ParseCmd(show_output, attributes)
                            output.message = cli_table.FormattedTable(width=91)
                        else:
                            output.message = show_output
                    except Exception as e:
                        self.log.error(str(e))
                        output.message = "Device not supported for show command"                  
                    finally:
                        self.log.info('Context: %s' % uinfo.context)



# ------------------------
# SERVICE CALLBACK EXAMPLE
# ------------------------
#class ServiceCallbacks(Service):

    # The create() callback is invoked inside NCS FASTMAP and
    # must always exist.
 #   @Service.create
 #   def cb_create(self, tctx, root, service, proplist):
 #      self.log.info('Service create(service=', service._path, ')')


    # The pre_modification() and post_modification() callbacks are optional,
    # and are invoked outside FASTMAP. pre_modification() is invoked before
    # create, update, or delete of the service, as indicated by the enum
    # ncs_service_operation op parameter. Conversely
    # post_modification() is invoked after create, update, or delete
    # of the service. These functions can be useful e.g. for
    # allocations that should be stored and existing also when the
    # service instance is removed.

    # @Service.pre_lock_create
    # def cb_pre_lock_create(self, tctx, root, service, proplist):
    #     self.log.info('Service plcreate(service=', service._path, ')')

    # @Service.pre_modification
    # def cb_pre_modification(self, tctx, op, kp, root, proplist):
    #     self.log.info('Service premod(service=', kp, ')')

    # @Service.post_modification
    # def cb_post_modification(self, tctx, op, kp, root, proplist):
    #     self.log.info('Service postmod(service=', kp, ')')


# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        self.log.info('Main RUNNING')
        self.register_action('show', Show)

    def teardown(self):
        self.log.info('Main FINISHED')
