./sqllogictest --engine ODBC3 --connection 'DSN=dolphindb;DRIVER={DolphinDB};SERVER=127.0.0.1;PORT=8848;UID=admin;PWD=123456;' /home/luwei/code/sqllogictest/testDolphin/select3.test > /home/luwei/code/sqllogictest/testDolphin/res/select3.test

./sqllogictest -verify /home/luwei/code/sqllogictest/testDolphin/res/select3.test


./sqllogictest --engine ODBC3 --connection 'DSN=dolphindb;DRIVER={DolphinDB};SERVER=127.0.0.1;PORT=8848;UID=admin;PWD=123456;' /home/luwei/code/sqllogictest/testDolphin/random/aggregates/slt_good_0.test > /home/luwei/code/sqllogictest/testDolphin/res/random/aggregates/slt_good_0.test