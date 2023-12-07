// Auto-generated. Do not edit!

// (in-package custom_msg_python.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let actimove = require('./actimove.js');

//-----------------------------------------------------------

class activmoveslist {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.listing = null;
    }
    else {
      if (initObj.hasOwnProperty('listing')) {
        this.listing = initObj.listing
      }
      else {
        this.listing = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type activmoveslist
    // Serialize message field [listing]
    // Serialize the length for message field [listing]
    bufferOffset = _serializer.uint32(obj.listing.length, buffer, bufferOffset);
    obj.listing.forEach((val) => {
      bufferOffset = actimove.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type activmoveslist
    let len;
    let data = new activmoveslist(null);
    // Deserialize message field [listing]
    // Deserialize array length for message field [listing]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.listing = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.listing[i] = actimove.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 48 * object.listing.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msg_python/activmoveslist';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ad5a8f0f1484d74e62d785ee2bf5ef94';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    custom_msg_python/actimove[] listing
    
    ================================================================================
    MSG: custom_msg_python/actimove
    custom_msg_python/blockdata block
    float32 humanprio
    float32 poscertainty
    float32 stabilety
    
    ================================================================================
    MSG: custom_msg_python/blockdata
    int32 xlen
    int32 ylen
    int32 zlen
    
    float32 xpos
    float32 ypos
    float32 zpos
    
    int32 rotation
    
    int32 blocktype
    int32 blockcolor
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new activmoveslist(null);
    if (msg.listing !== undefined) {
      resolved.listing = new Array(msg.listing.length);
      for (let i = 0; i < resolved.listing.length; ++i) {
        resolved.listing[i] = actimove.Resolve(msg.listing[i]);
      }
    }
    else {
      resolved.listing = []
    }

    return resolved;
    }
};

module.exports = activmoveslist;
