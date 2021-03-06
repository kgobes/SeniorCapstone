// Generated by gencpp from file lili_audio/RecognizeSpeechResponse.msg
// DO NOT EDIT!


#ifndef LILI_AUDIO_MESSAGE_RECOGNIZESPEECHRESPONSE_H
#define LILI_AUDIO_MESSAGE_RECOGNIZESPEECHRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace lili_audio
{
template <class ContainerAllocator>
struct RecognizeSpeechResponse_
{
  typedef RecognizeSpeechResponse_<ContainerAllocator> Type;

  RecognizeSpeechResponse_()
    : speech()  {
    }
  RecognizeSpeechResponse_(const ContainerAllocator& _alloc)
    : speech(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _speech_type;
  _speech_type speech;




  typedef boost::shared_ptr< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> const> ConstPtr;

}; // struct RecognizeSpeechResponse_

typedef ::lili_audio::RecognizeSpeechResponse_<std::allocator<void> > RecognizeSpeechResponse;

typedef boost::shared_ptr< ::lili_audio::RecognizeSpeechResponse > RecognizeSpeechResponsePtr;
typedef boost::shared_ptr< ::lili_audio::RecognizeSpeechResponse const> RecognizeSpeechResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace lili_audio

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'lili_audio': ['/home/christie/catkin_ws/devel/share/lili_audio/msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0f212b08e2dfacb9148fa1a62023e9ac";
  }

  static const char* value(const ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0f212b08e2dfacb9ULL;
  static const uint64_t static_value2 = 0x148fa1a62023e9acULL;
};

template<class ContainerAllocator>
struct DataType< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "lili_audio/RecognizeSpeechResponse";
  }

  static const char* value(const ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string speech\n\
\n\
";
  }

  static const char* value(const ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.speech);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RecognizeSpeechResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::lili_audio::RecognizeSpeechResponse_<ContainerAllocator>& v)
  {
    s << indent << "speech: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.speech);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LILI_AUDIO_MESSAGE_RECOGNIZESPEECHRESPONSE_H
