// Auto-generated. Do not edit!

// (in-package lili_audio.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class RecognizeSpeechRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RecognizeSpeechRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RecognizeSpeechRequest
    let len;
    let data = new RecognizeSpeechRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'lili_audio/RecognizeSpeechRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RecognizeSpeechRequest(null);
    return resolved;
    }
};

class RecognizeSpeechResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.speech = null;
    }
    else {
      if (initObj.hasOwnProperty('speech')) {
        this.speech = initObj.speech
      }
      else {
        this.speech = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RecognizeSpeechResponse
    // Serialize message field [speech]
    bufferOffset = _serializer.string(obj.speech, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RecognizeSpeechResponse
    let len;
    let data = new RecognizeSpeechResponse(null);
    // Deserialize message field [speech]
    data.speech = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.speech.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'lili_audio/RecognizeSpeechResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0f212b08e2dfacb9148fa1a62023e9ac';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string speech
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RecognizeSpeechResponse(null);
    if (msg.speech !== undefined) {
      resolved.speech = msg.speech;
    }
    else {
      resolved.speech = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: RecognizeSpeechRequest,
  Response: RecognizeSpeechResponse,
  md5sum() { return '0f212b08e2dfacb9148fa1a62023e9ac'; },
  datatype() { return 'lili_audio/RecognizeSpeech'; }
};
