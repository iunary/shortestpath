import mongoengine as me


class Trip(me.Document):
    """
    Trip document definition
    """

    name = me.StringField(max_length=255, required=True)
    business = me.BooleanField(required=True)
    destinations = me.ListField(me.StringField(max_length=255), required=True)
    places_to_travel = me.ListField(me.StringField(max_length=255), required=True)
