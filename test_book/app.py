import pytest
from test_book.common.utils import case_path, report_path, get_time
t = get_time()
# pytest.main(['-v',f'--html={report_path}/{t}.html', case_path])
# pytest.main(['-v', f'--html={report_path}/{t}.html', case_path])
# pytest.main(['-v', '--html=report/t.html', case_path])
pytest.main(['-vs', 'case/test_login.py'])
