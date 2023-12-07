// Generated by gencpp from file custom_msg_python/custom.msg
// DO NOT EDIT!


#ifndef CUSTOM_MSG_PYTHON_MESSAGE_CUSTOM_H
#define CUSTOM_MSG_PYTHON_MESSAGE_CUSTOM_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace custom_msg_python
{
template <class ContainerAllocator>
struct custom_
{
  typedef custom_<ContainerAllocator> Type;

  custom_()
    : configurationmode(false)  {
    }
  custom_(const ContainerAllocator& _alloc)
    : configurationmode(false)  {
  (void)_alloc;
    }



   typedef uint8_t _configurationmode_type;
  _configurationmode_type configurationmode;





  typedef boost::shared_ptr< ::custom_msg_python::custom_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::custom_msg_python::custom_<ContainerAllocator> const> ConstPtr;

}; // struct custom_

typedef ::custom_msg_python::custom_<std::allocator<void> > custom;

typedef boost::shared_ptr< ::custom_msg_python::custom > customPtr;
typedef boost::shared_ptr< ::custom_msg_python::custom const> customConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::custom_msg_python::custom_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::custom_msg_python::custom_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::custom_msg_python::custom_<ContainerAllocator1> & lhs, const ::custom_msg_python::custom_<ContainerAllocator2> & rhs)
{
  return lhs.configurationmode == rhs.configurationmode;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::custom_msg_python::custom_<ContainerAllocator1> & lhs, const ::custom_msg_python::custom_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace custom_msg_python

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::custom_msg_python::custom_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::custom_msg_python::custom_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::custom_msg_python::custom_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::custom_msg_python::custom_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::custom_msg_python::custom_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::custom_msg_python::custom_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::custom_msg_python::custom_<ContainerAllocator> >
{
  static const char* value()
  {
    return "63b9c1c4bde05e435d92eaf6475fe3c0";
  }

  static const char* value(const ::custom_msg_python::custom_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x63b9c1c4bde05e43ULL;
  static const uint64_t static_value2 = 0x5d92eaf6475fe3c0ULL;
};

template<class ContainerAllocator>
struct DataType< ::custom_msg_python::custom_<ContainerAllocator> >
{
  static const char* value()
  {
    return "custom_msg_python/custom";
  }

  static const char* value(const ::custom_msg_python::custom_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::custom_msg_python::custom_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
"bool configurationmode\n"
;
  }

  static const char* value(const ::custom_msg_python::custom_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::custom_msg_python::custom_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.configurationmode);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct custom_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::custom_msg_python::custom_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::custom_msg_python::custom_<ContainerAllocator>& v)
  {
    s << indent << "configurationmode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.configurationmode);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CUSTOM_MSG_PYTHON_MESSAGE_CUSTOM_H
