// Require discord.js package
const Discord = require("discord.js");

// Create a new client using the new keyword
const DiscordClient = new Discord.Client();

// Channel ID to write the message in
const channelID = "538068749400539146";

// Clean code array
const cleanArray = [
  "./token.json",
  "ready",
  "message",
  "!help",
  "!object",
  "reconnecting",
];

// Add a safer way to store the token (password)
const { token } = require(cleanArray[0]);

// Display a message when the bot comes online, fired once
DiscordClient.on(cleanArray[1], () => {
  console.log(`Logged in as ${DiscordClient.user.tag}!`);
});

// Reconnecting event
DiscordClient.on(cleanArray[5], () => {
  console.log(`This bot is trying to reconnect: ${DiscordClient.user.tag}!`);
});

// Message event
DiscordClient.on(cleanArray[2], async (msg) => {
  // Failsafe
  const msgToLower = msg.content.toLowerCase();

  // console log the object when writing a specific command
  if (msgToLower.includes(cleanArray[4]) && msg.author.bot === false) {
    // The id needs to be an id that your channel uses.

    // Find id by the console log statement below

    console.log(msg.channel);

    DiscordClient.channels.cache
      .get(channelID)
      .send(
        "Hello, someone used the !object command in a text-channel called " +
          msg.channel.name +
          " in a server called " +
          msg.channel.guild.name
      );
  }

  // !help command
  else if (msgToLower === cleanArray[3]) {
    msg.reply(
      "This bot has 2 commands: !help and the second command needs to contain the word 'hello'"
    );
  }
});

// Token (password)
DiscordClient.login(token);
