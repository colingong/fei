# Tokens for drf                                 UserID
# '1c664c37a16abd4e555db5da95ab02e59a0e68dc',    '18'
# '50fd860b67d2d2e93264477fa2c3ecf5cad8672f',    '29'
# '9549d987de7a783caeb5a624345dd0b519a54515',    '26'
# 'a689fd100f8cce0518dc9e2db7d830f5f9d720d7',    '27'
# 'c9a90d010872edec8fb38433fbd88e0adf53eebb',    '1'
# 'cbb8823d95cdaf6b575375abde01c9510f17ebe6',    '25'
# 'fb4fa62ad04f27e563b76c376c92079116a7d14f',    '28'


curl -X GET -H 'Authorization: Token 9549d987de7a783caeb5a624345dd0b519a54515' http://127.0.0.1:8000/v2/ 
# curl -X GET http://127.0.0.1:8000/v2/ -H 'Authorization: Token 9549d987de7a783caeb5a624345dd0b519a54515'
# curl -X POST http://127.0.0.1:8000/v2/new/product/ -H 'Authorization: Token 9549d987de7a783caeb5a624345dd0b519a54515' \
#          -d  '{"category": 1,"warehouse": 4,"product_name": "奥利奥饼干100-1","product_description": "奥利奥夹心饼干100克","product_price": "5.00","product_stock": 200}'
