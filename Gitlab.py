import shodan


# Configuration
API_KEY = "Your API Key"
SEARCH_FOR = 'product:"GitLab Self-Managed"'
try:
        # Setup the api
		api = shodan.Shodan(API_KEY)

        # Perform the search
		result = api.search(SEARCH_FOR, limit=1000)

        # Loop through the matches and print each IP
		for service in result['matches']:
				IP = service['ip_str']
				CC = service['location']['country_name']
				PORT = str(service['port'])
				test_cam (IP,PORT,CC)
				

				
except KeyboardInterrupt:
		print ("Ctrl-c pressed ...")
		sys.exit(1)
				
except Exception as e:
		print('Error: %s' % e)
		sys.exit(1)
