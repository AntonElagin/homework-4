run: # Предварительно засовываем в env пароль (export PASSWORD=твой пароль export LOGIN=твой логин)
	sh node.sh &
	sleep 1
	python3 run_tests.py