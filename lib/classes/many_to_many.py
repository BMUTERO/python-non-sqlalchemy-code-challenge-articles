class Band:

    all_bands = []

    def __init__(self, name, hometown):
        self._name = None
        self._hometown = None
        self.name = name
        self.hometown = hometown
        Band.all_bands.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, value):
        if isinstance(value, str) and len(value) == 0:
            return 
        if hasattr(self, '_hometown') and self._hometown is not None:
            return
        self._hometown = value
    def concerts(self):
        band_concerts = [concert for concert in Concert.all_concerts if concert.band == self]
        return band_concerts if band_concerts else None

    def venues(self):
        if not self.concerts():
            return None
        unique_venues = []
        seen = set()
        for concert in self.concerts():
            if concert.venue not in seen:
                unique_venues.append(concert.venue)
                seen.add(concert.venue)
        return unique_venues if unique_venues else None

    def play_in_venue(self, venue, date):
        new_concert = Concert(date, self, venue)
        return new_concert

    def all_introductions(self):
        if not self.concerts():
            return None
        return [concert.introduction() for concert in self.concerts()]

