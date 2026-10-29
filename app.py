
import aws_cdk as cdk

from hr_leave_portal.backend_stack import BackendStack

app = cdk.App()

BackendStack(app, "HrLeavePortalBackend")

app.synth()