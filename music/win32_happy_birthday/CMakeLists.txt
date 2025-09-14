cmake_minimum_required(VERSION 3.10)

project(MidiHappyBirthday C)

add_executable(wi32_midi_happy_birthday main.c)

if(MSVC)
    target_compile_options(wi32_midi_happy_birthday PRIVATE /W4)
else()
    target_compile_options(wi32_midi_happy_birthday PRIVATE -Wall -Wextra -Wpedantic)
endif()

target_link_libraries(wi32_midi_happy_birthday PRIVATE winmm)

