from importsAndConfigs import ma 

class MatchSchema(ma.Schema):
	class Meta:
		fields = (
				'id',
				'id_user',
                'stage',
                'match_prediction',
				)