import { 
  User, InsertUser,
  Destination, InsertDestination,
  PropertyType, InsertPropertyType,
  Property, InsertProperty,
  RoomType, InsertRoomType,
  Booking, InsertBooking,
  SearchParam, InsertSearchParam,
  TravelInspiration, InsertTravelInspiration
} from "@shared/schema";
import { destinations, propertyTypes, featuredProperties, roomTypes, travelInspirations } from "../client/src/lib/mock-data";

export interface IStorage {
  // User operations
  getUser(id: number): Promise<User | undefined>;
  getUserByUsername(username: string): Promise<User | undefined>;
  createUser(user: InsertUser): Promise<User>;

  // Destination operations
  getDestinations(): Promise<Destination[]>;
  getDestination(id: number): Promise<Destination | undefined>;
  createDestination(destination: InsertDestination): Promise<Destination>;

  // Property Type operations
  getPropertyTypes(): Promise<PropertyType[]>;
  getPropertyType(id: number): Promise<PropertyType | undefined>;
  createPropertyType(propertyType: InsertPropertyType): Promise<PropertyType>;

  // Property operations
  getProperties(): Promise<Property[]>;
  getProperty(id: number): Promise<Property | undefined>;
  getPropertiesByDestination(destinationId: number): Promise<Property[]>;
  getPropertiesByType(propertyTypeId: number): Promise<Property[]>;
  getFeaturedProperties(): Promise<Property[]>;
  createProperty(property: InsertProperty): Promise<Property>;
  searchProperties(params: {
    destination?: string;
    checkIn?: Date;
    checkOut?: Date;
    adults?: number;
    children?: number;
    rooms?: number;
  }): Promise<Property[]>;

  // Room Type operations
  getRoomTypes(propertyId: number): Promise<RoomType[]>;
  getRoomType(id: number): Promise<RoomType | undefined>;
  createRoomType(roomType: InsertRoomType): Promise<RoomType>;

  // Booking operations
  getBookings(userId?: number): Promise<Booking[]>;
  getBooking(id: number): Promise<Booking | undefined>;
  createBooking(booking: InsertBooking): Promise<Booking>;
  updateBookingStatus(id: number, status: string): Promise<Booking | undefined>;

  // Search Parameters operations
  saveSearchParams(searchParam: InsertSearchParam): Promise<SearchParam>;
  getRecentSearchParams(userId?: number, limit?: number): Promise<SearchParam[]>;

  // Travel Inspiration operations
  getTravelInspirations(): Promise<TravelInspiration[]>;
  createTravelInspiration(inspiration: InsertTravelInspiration): Promise<TravelInspiration>;
  
  // Database seeding operation
  seedDatabase(): Promise<void>;
}

// In-memory storage implementation
export class MemStorage implements IStorage {
  private users: Map<number, User> = new Map();
  private destinations: Map<number, Destination> = new Map();
  private propertyTypes: Map<number, PropertyType> = new Map();
  private properties: Map<number, Property> = new Map();
  private roomTypes: Map<number, RoomType> = new Map();
  private bookings: Map<number, Booking> = new Map();
  private searchParams: Map<number, SearchParam> = new Map();
  private travelInspirations: Map<number, TravelInspiration> = new Map();
  
  private currentUserId = 1;
  private currentDestinationId = 1;
  private currentPropertyTypeId = 1;
  private currentPropertyId = 1;
  private currentRoomTypeId = 1;
  private currentBookingId = 1;
  private currentSearchParamId = 1;
  private currentTravelInspirationId = 1;

  constructor() {
    this.initializeMockData();
  }

  async getUser(id: number): Promise<User | undefined> {
    return this.users.get(id);
  }

  async getUserByUsername(username: string): Promise<User | undefined> {
    for (const user of this.users.values()) {
      if (user.username === username) {
        return user;
      }
    }
    return undefined;
  }

  async createUser(insertUser: InsertUser): Promise<User> {
    const id = this.currentUserId++;
    const user: User = { ...insertUser, id };
    this.users.set(id, user);
    return user;
  }

  async getDestinations(): Promise<Destination[]> {
    return Array.from(this.destinations.values());
  }

  async getDestination(id: number): Promise<Destination | undefined> {
    return this.destinations.get(id);
  }

  async createDestination(destination: InsertDestination): Promise<Destination> {
    const id = this.currentDestinationId++;
    const newDestination: Destination = { ...destination, id };
    this.destinations.set(id, newDestination);
    return newDestination;
  }

  async getPropertyTypes(): Promise<PropertyType[]> {
    return Array.from(this.propertyTypes.values());
  }

  async getPropertyType(id: number): Promise<PropertyType | undefined> {
    return this.propertyTypes.get(id);
  }

  async createPropertyType(propertyType: InsertPropertyType): Promise<PropertyType> {
    const id = this.currentPropertyTypeId++;
    const newPropertyType: PropertyType = { ...propertyType, id };
    this.propertyTypes.set(id, newPropertyType);
    return newPropertyType;
  }

  async getProperties(): Promise<Property[]> {
    return Array.from(this.properties.values());
  }

  async getProperty(id: number): Promise<Property | undefined> {
    return this.properties.get(id);
  }

  async getPropertiesByDestination(destinationId: number): Promise<Property[]> {
    return Array.from(this.properties.values()).filter(p => p.destinationId === destinationId);
  }

  async getPropertiesByType(propertyTypeId: number): Promise<Property[]> {
    return Array.from(this.properties.values()).filter(p => p.propertyTypeId === propertyTypeId);
  }

  async getFeaturedProperties(): Promise<Property[]> {
    // Return first 8 properties as featured
    return Array.from(this.properties.values()).slice(0, 8);
  }

  async createProperty(property: InsertProperty): Promise<Property> {
    const id = this.currentPropertyId++;
    const newProperty: Property = { ...property, id };
    this.properties.set(id, newProperty);
    return newProperty;
  }

  async searchProperties(params: {
    destination?: string;
    checkIn?: Date;
    checkOut?: Date;
    adults?: number;
    children?: number;
    rooms?: number;
  }): Promise<Property[]> {
    let results = Array.from(this.properties.values());

    if (params.destination) {
      const destinationLower = params.destination.toLowerCase();
      results = results.filter(property => {
        const destination = this.destinations.get(property.destinationId);
        return destination?.name.toLowerCase().includes(destinationLower);
      });
    }

    // Basic filtering - in a real app you'd have more sophisticated availability checking
    return results;
  }

  async getRoomTypes(propertyId: number): Promise<RoomType[]> {
    return Array.from(this.roomTypes.values()).filter(rt => rt.propertyId === propertyId);
  }

  async getRoomType(id: number): Promise<RoomType | undefined> {
    return this.roomTypes.get(id);
  }

  async createRoomType(roomType: InsertRoomType): Promise<RoomType> {
    const id = this.currentRoomTypeId++;
    const newRoomType: RoomType = { ...roomType, id };
    this.roomTypes.set(id, newRoomType);
    return newRoomType;
  }

  async getBookings(userId?: number): Promise<Booking[]> {
    let bookings = Array.from(this.bookings.values());
    if (userId) {
      bookings = bookings.filter(b => b.userId === userId);
    }
    return bookings;
  }

  async getBooking(id: number): Promise<Booking | undefined> {
    return this.bookings.get(id);
  }

  async createBooking(booking: InsertBooking): Promise<Booking> {
    const id = this.currentBookingId++;
    const newBooking: Booking = { 
      ...booking, 
      id,
      createdAt: new Date(),
      status: booking.status || "confirmed"
    };
    this.bookings.set(id, newBooking);
    return newBooking;
  }

  async updateBookingStatus(id: number, status: string): Promise<Booking | undefined> {
    const booking = this.bookings.get(id);
    if (booking) {
      booking.status = status;
      this.bookings.set(id, booking);
    }
    return booking;
  }

  async saveSearchParams(searchParam: InsertSearchParam): Promise<SearchParam> {
    const id = this.currentSearchParamId++;
    const newSearchParam: SearchParam = { 
      ...searchParam, 
      id,
      createdAt: new Date()
    };
    this.searchParams.set(id, newSearchParam);
    return newSearchParam;
  }

  async getRecentSearchParams(userId?: number, limit: number = 5): Promise<SearchParam[]> {
    let params = Array.from(this.searchParams.values());
    if (userId) {
      params = params.filter(p => p.userId === userId);
    }
    return params
      .sort((a, b) => (b.createdAt?.getTime() || 0) - (a.createdAt?.getTime() || 0))
      .slice(0, limit);
  }

  async getTravelInspirations(): Promise<TravelInspiration[]> {
    return Array.from(this.travelInspirations.values());
  }

  async createTravelInspiration(inspiration: InsertTravelInspiration): Promise<TravelInspiration> {
    const id = this.currentTravelInspirationId++;
    const newInspiration: TravelInspiration = { ...inspiration, id };
    this.travelInspirations.set(id, newInspiration);
    return newInspiration;
  }

  async seedDatabase(): Promise<void> {
    console.log("Database already seeded, skipping...");
  }

  private initializeMockData() {
    // Initialize destinations
    destinations.forEach(dest => {
      this.destinations.set(dest.id, dest);
      if (dest.id >= this.currentDestinationId) {
        this.currentDestinationId = dest.id + 1;
      }
    });

    // Initialize property types
    propertyTypes.forEach(type => {
      this.propertyTypes.set(type.id, type);
      if (type.id >= this.currentPropertyTypeId) {
        this.currentPropertyTypeId = type.id + 1;
      }
    });

    // Initialize properties
    featuredProperties.forEach(prop => {
      this.properties.set(prop.id, prop);
      if (prop.id >= this.currentPropertyId) {
        this.currentPropertyId = prop.id + 1;
      }
    });

    // Initialize room types
    roomTypes.forEach(room => {
      this.roomTypes.set(room.id, room);
      if (room.id >= this.currentRoomTypeId) {
        this.currentRoomTypeId = room.id + 1;
      }
    });

    // Initialize travel inspirations
    travelInspirations.forEach(inspiration => {
      this.travelInspirations.set(inspiration.id, inspiration);
      if (inspiration.id >= this.currentTravelInspirationId) {
        this.currentTravelInspirationId = inspiration.id + 1;
      }
    });
  }
}

export const storage = new MemStorage();