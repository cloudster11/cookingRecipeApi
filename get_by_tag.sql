SELECT * FROM RecHasTag
GROUP BY RecHasTag.ID_Rec
HAVING 	SUM(RecHasTag.ID_Tag = 1) > 0 AND
		SUM(RecHasTag.ID_Tag = 2) > 0 AND
		SUM(RecHasTag.ID_Tag = 3) > 0
