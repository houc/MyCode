from SCRM.workbench.work_effectiveness_st import WorkEffectiveness
from SCRM.jurisdiction.company_manage_st import CompanyManage
from SCRM.jurisdiction.coordination_app_st import CoordinationApp
from SCRM.login.login_repeat_st import TestLogin
from SCRM.report_test.report_check_failed_st import TestCheckFailed
from SCRM.report_test.report_check_skipped_st import TestCheckSkipped
from SCRM.workbench.three_table_st import ThreeTable
from SCRM.workbench.shortcut_function_st import ShortcutFunction
from SCRM.jurisdiction.sale_manage_st import SaleManage
from SCRM.public_test.method_up_st import TestPublicMethod
from SCRM.report_test.report_check_errors_st import TestCheckErrors
from SCRM.report_test.report_check_success_st import TestCheckSuccess


__all__ = {CompanyManage, TestPublicMethod, SaleManage, TestCheckSkipped, WorkEffectiveness, TestLogin, ThreeTable, TestCheckErrors, TestCheckSuccess, TestCheckFailed, CoordinationApp, ShortcutFunction}