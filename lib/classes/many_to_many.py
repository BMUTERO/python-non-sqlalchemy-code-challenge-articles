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

class Concert:

    all_concerts = []
    all = []

    def __init__(self, date, band, venue):
        self._date = None
        self._band = None
        self._venue = None
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all_concerts.append(self)
        Concert.all.append(self)
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value

    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"   

class Venue:

    all_venues = []

    def __init__(self, name, city):
        self._name = None
        self._city = None
        self.name = name
        self.city = city
        Venue.all_venues.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value

    def concerts(self):
        venue_concerts = [concert for concert in Concert.all_concerts if concert.venue == self]
        return venue_concerts if venue_concerts else None

    def bands(self):
        if not self.concerts():
            return None
        unique_bands = []
        seen = set()
        for concert in self.concerts():
            if concert.band not in seen:
                unique_bands.append(concert.band)
                seen.add(concert.band)
        return unique_bands if unique_bands else None
    
    def concert_on(self, date):
        venue_concerts = self.concerts()
        if not venue_concerts:
            return None
        for concert in venue_concerts:
            if concert.date == date:
                return concert
        return None
    
