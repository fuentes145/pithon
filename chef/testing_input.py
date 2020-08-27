import unittest.mock 

mock = unittest.mock.MagicMock()


mock.side_effect = iter(['2',
                    '58943',
                    '83445'
                    ])

N = int(mock())
for i in range(N):
    print(int(mock()))
