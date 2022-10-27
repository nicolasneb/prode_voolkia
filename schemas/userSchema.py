from importsAndConfigs import ma 

class UserSchema(ma.Schema):
	class Meta:
		fields = (
				'id',
				'username',
                'password_hash'
				)