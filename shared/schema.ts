import { pgTable, text, integer, timestamp, boolean, decimal, real, json } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod";

// Users table
export const users = pgTable("users", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  username: text("username").notNull().unique(),
  email: text("email").notNull().unique(),
  password: text("password").notNull(),
  firstName: text("first_name"),
  lastName: text("last_name"),
  phone: text("phone"),
  dateOfBirth: timestamp("date_of_birth"),
  createdAt: timestamp("created_at").defaultNow(),
});

// Park areas/zones
export const parkAreas = pgTable("park_areas", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  name: text("name").notNull(),
  description: text("description"),
  imageUrl: text("image_url"),
  mapCoordinates: json("map_coordinates"), // {x: number, y: number, width: number, height: number}
  theme: text("theme"), // fantasyland, tomorrowland, adventureland, etc
  color: text("color").default("#3B82F6"), // for map display
});

// Attraction categories
export const attractionCategories = pgTable("attraction_categories", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  name: text("name").notNull(),
  description: text("description"),
  icon: text("icon"), // lucide icon name
  color: text("color").default("#3B82F6"),
});

// Attractions table
export const attractions = pgTable("attractions", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  name: text("name").notNull(),
  description: text("description"),
  shortDescription: text("short_description"),
  categoryId: integer("category_id").references(() => attractionCategories.id),
  areaId: integer("area_id").references(() => parkAreas.id),
  imageUrl: text("image_url"),
  galleryImages: json("gallery_images").$type<string[]>(),
  mapCoordinates: json("map_coordinates"), // {x: number, y: number}
  
  // Ride specifications
  minHeight: integer("min_height"), // in cm
  maxHeight: integer("max_height"), // in cm
  duration: integer("duration"), // in minutes
  capacity: integer("capacity"), // per ride
  thrillLevel: integer("thrill_level"), // 1-5 scale
  
  // Status and operations
  isActive: boolean("is_active").default(true),
  waitTime: integer("wait_time").default(0), // current wait time in minutes
  fastPassAvailable: boolean("fast_pass_available").default(false),
  
  // Accessibility
  wheelchairAccessible: boolean("wheelchair_accessible").default(false),
  hearingImpairedAccess: boolean("hearing_impaired_access").default(false),
  visuallyImpairedAccess: boolean("visually_impaired_access").default(false),
  
  // Ratings and reviews
  rating: real("rating").default(0),
  reviewCount: integer("review_count").default(0),
  
  // Operational hours
  openTime: text("open_time"), // "09:00"
  closeTime: text("close_time"), // "22:00"
  
  createdAt: timestamp("created_at").defaultNow(),
  updatedAt: timestamp("updated_at").defaultNow(),
});

// Restaurants in the park
export const restaurants = pgTable("restaurants", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  name: text("name").notNull(),
  description: text("description"),
  areaId: integer("area_id").references(() => parkAreas.id),
  imageUrl: text("image_url"),
  mapCoordinates: json("map_coordinates"),
  cuisine: text("cuisine"), // mexican, italian, american, etc
  priceRange: integer("price_range"), // 1-4 scale ($, $$, $$$, $$$$)
  rating: real("rating").default(0),
  reviewCount: integer("review_count").default(0),
  isActive: boolean("is_active").default(true),
  openTime: text("open_time"),
  closeTime: text("close_time"),
});

// Events and shows
export const events = pgTable("events", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  name: text("name").notNull(),
  description: text("description"),
  areaId: integer("area_id").references(() => parkAreas.id),
  imageUrl: text("image_url"),
  mapCoordinates: json("map_coordinates"),
  eventType: text("event_type"), // show, parade, meet-greet, special-event
  duration: integer("duration"), // in minutes
  capacity: integer("capacity"),
  isRecurring: boolean("is_recurring").default(false),
  showTimes: json("show_times").$type<string[]>(), // ["10:00", "14:00", "18:00"]
  startDate: timestamp("start_date"),
  endDate: timestamp("end_date"),
  ticketRequired: boolean("ticket_required").default(false),
  isActive: boolean("is_active").default(true),
});

// Ticket types
export const ticketTypes = pgTable("ticket_types", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  name: text("name").notNull(),
  description: text("description"),
  price: decimal("price", { precision: 10, scale: 2 }),
  type: text("type"), // single-day, multi-day, season-pass, fast-pass
  validDays: integer("valid_days").default(1),
  includes: json("includes").$type<string[]>(), // ["park-access", "fast-pass", "parking"]
  isActive: boolean("is_active").default(true),
});

// User tickets/passes
export const userTickets = pgTable("user_tickets", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  userId: integer("user_id").references(() => users.id),
  ticketTypeId: integer("ticket_type_id").references(() => ticketTypes.id),
  purchaseDate: timestamp("purchase_date").defaultNow(),
  validFrom: timestamp("valid_from"),
  validUntil: timestamp("valid_until"),
  isUsed: boolean("is_used").default(false),
  qrCode: text("qr_code"),
  totalPrice: decimal("total_price", { precision: 10, scale: 2 }),
});

// Wait times log for analytics
export const waitTimes = pgTable("wait_times", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  attractionId: integer("attraction_id").references(() => attractions.id),
  waitTime: integer("wait_time"), // in minutes
  timestamp: timestamp("timestamp").defaultNow(),
});

// User favorites
export const userFavorites = pgTable("user_favorites", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  userId: integer("user_id").references(() => users.id),
  attractionId: integer("attraction_id").references(() => attractions.id),
  createdAt: timestamp("created_at").defaultNow(),
});

// User reviews
export const attractionReviews = pgTable("attraction_reviews", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  userId: integer("user_id").references(() => users.id),
  attractionId: integer("attraction_id").references(() => attractions.id),
  rating: integer("rating"), // 1-5 stars
  comment: text("comment"),
  createdAt: timestamp("created_at").defaultNow(),
});

// Park services (restrooms, first aid, etc)
export const parkServices = pgTable("park_services", {
  id: integer("id").primaryKey().generatedByDefaultAsIdentity(),
  name: text("name").notNull(),
  type: text("type"), // restroom, first-aid, atm, gift-shop, photo-spot
  areaId: integer("area_id").references(() => parkAreas.id),
  mapCoordinates: json("map_coordinates"),
  icon: text("icon"), // lucide icon name
  isActive: boolean("is_active").default(true),
});

// Insert schemas
export const insertUserSchema = createInsertSchema(users).pick({
  username: true,
  email: true,
  password: true,
  firstName: true,
  lastName: true,
  phone: true,
  dateOfBirth: true,
});

export const insertParkAreaSchema = createInsertSchema(parkAreas).pick({
  name: true,
  description: true,
  imageUrl: true,
  mapCoordinates: true,
  theme: true,
  color: true,
});

export const insertAttractionCategorySchema = createInsertSchema(attractionCategories).pick({
  name: true,
  description: true,
  icon: true,
  color: true,
});

export const insertAttractionSchema = createInsertSchema(attractions).pick({
  name: true,
  description: true,
  shortDescription: true,
  categoryId: true,
  areaId: true,
  imageUrl: true,
  galleryImages: true,
  mapCoordinates: true,
  minHeight: true,
  maxHeight: true,
  duration: true,
  capacity: true,
  thrillLevel: true,
  isActive: true,
  waitTime: true,
  fastPassAvailable: true,
  wheelchairAccessible: true,
  hearingImpairedAccess: true,
  visuallyImpairedAccess: true,
  rating: true,
  reviewCount: true,
  openTime: true,
  closeTime: true,
});

export const insertRestaurantSchema = createInsertSchema(restaurants).pick({
  name: true,
  description: true,
  areaId: true,
  imageUrl: true,
  mapCoordinates: true,
  cuisine: true,
  priceRange: true,
  rating: true,
  reviewCount: true,
  isActive: true,
  openTime: true,
  closeTime: true,
});

export const insertEventSchema = createInsertSchema(events).pick({
  name: true,
  description: true,
  areaId: true,
  imageUrl: true,
  mapCoordinates: true,
  eventType: true,
  duration: true,
  capacity: true,
  isRecurring: true,
  showTimes: true,
  startDate: true,
  endDate: true,
  ticketRequired: true,
  isActive: true,
});

export const insertTicketTypeSchema = createInsertSchema(ticketTypes).pick({
  name: true,
  description: true,
  price: true,
  type: true,
  validDays: true,
  includes: true,
  isActive: true,
});

export const insertUserTicketSchema = createInsertSchema(userTickets).pick({
  userId: true,
  ticketTypeId: true,
  validFrom: true,
  validUntil: true,
  totalPrice: true,
});

export const insertWaitTimeSchema = createInsertSchema(waitTimes).pick({
  attractionId: true,
  waitTime: true,
});

export const insertUserFavoriteSchema = createInsertSchema(userFavorites).pick({
  userId: true,
  attractionId: true,
});

export const insertAttractionReviewSchema = createInsertSchema(attractionReviews).pick({
  userId: true,
  attractionId: true,
  rating: true,
  comment: true,
});

export const insertParkServiceSchema = createInsertSchema(parkServices).pick({
  name: true,
  type: true,
  areaId: true,
  mapCoordinates: true,
  icon: true,
  isActive: true,
});

// Type exports
export type User = typeof users.$inferSelect;
export type InsertUser = z.infer<typeof insertUserSchema>;

export type ParkArea = typeof parkAreas.$inferSelect;
export type InsertParkArea = z.infer<typeof insertParkAreaSchema>;

export type AttractionCategory = typeof attractionCategories.$inferSelect;
export type InsertAttractionCategory = z.infer<typeof insertAttractionCategorySchema>;

export type Attraction = typeof attractions.$inferSelect;
export type InsertAttraction = z.infer<typeof insertAttractionSchema>;

export type Restaurant = typeof restaurants.$inferSelect;
export type InsertRestaurant = z.infer<typeof insertRestaurantSchema>;

export type Event = typeof events.$inferSelect;
export type InsertEvent = z.infer<typeof insertEventSchema>;

export type TicketType = typeof ticketTypes.$inferSelect;
export type InsertTicketType = z.infer<typeof insertTicketTypeSchema>;

export type UserTicket = typeof userTickets.$inferSelect;
export type InsertUserTicket = z.infer<typeof insertUserTicketSchema>;

export type WaitTime = typeof waitTimes.$inferSelect;
export type InsertWaitTime = z.infer<typeof insertWaitTimeSchema>;

export type UserFavorite = typeof userFavorites.$inferSelect;
export type InsertUserFavorite = z.infer<typeof insertUserFavoriteSchema>;

export type AttractionReview = typeof attractionReviews.$inferSelect;
export type InsertAttractionReview = z.infer<typeof insertAttractionReviewSchema>;

export type ParkService = typeof parkServices.$inferSelect;
export type InsertParkService = z.infer<typeof insertParkServiceSchema>;