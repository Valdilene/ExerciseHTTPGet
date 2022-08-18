from download import download_csv_to_dict

TEST_CSV_URL='https://gist.githubusercontent.com/chriddyp/feaa84b34854e53fb72a/raw/dbba00aeafb981f0f50014030d1b6ad0399d957d/example-data.csv'

the_dict_from_remote_url = download_csv_to_dict(TEST_CSV_URL)

if the_dict_from_remote_url is None:
  exit(1)

index = 0
for row in the_dict_from_remote_url:
  print(index, row)
  print('- '*30)
  index += 1