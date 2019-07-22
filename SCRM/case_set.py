from SCRM.report_test.report_check_errors_st import TestCheckErrors
from SCRM.login.login_repeat_st import TestLogin
from SCRM.workbench.three_table_st import ThreeTable
from SCRM.jurisdiction.coordination_app_st import CoordinationApp
from SCRM.workbench.shortcut_function_st import ShortcutFunction
from SCRM.report_test.report_check_failed_st import TestCheckFailed
from SCRM.report_test.report_check_success_st import TestCheckSuccess
from SCRM.jurisdiction.company_manage_st import CompanyManage
from SCRM.report_test.report_check_skipped_st import TestCheckSkipped
from SCRM.jurisdiction.sale_manage_st import SaleManage
from SCRM.workbench.work_effectiveness_st import WorkEffectiveness
from SCRM.public_test.method_up_st import TestPublicMethod


__all__ = {TestCheckErrors, CompanyManage, ThreeTable, TestPublicMethod, TestCheckSkipped, WorkEffectiveness, ShortcutFunction, TestCheckFailed, TestCheckSuccess, CoordinationApp, SaleManage, TestLogin}