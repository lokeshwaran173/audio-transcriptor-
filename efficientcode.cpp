#include <iostream>
#include <sphinxbase/ad.h>
#include <sphinxbase/err.h>
#include <sphinxbase/pocketphinx.h>

// Define a callback function for speech recognition results
static void recognition_callback(void* user_data, const char* hypothesis) {
    if (hypothesis != nullptr) {
        // Print the recognized text
        std::cout << "Recognized: " << hypothesis << std::endl;

        // Perform translation (you should replace this with a real translation function)
        std::string translation = translateToEnglish(hypothesis);
        std::cout << "Translation: " << translation << std::endl;
    }
}

// Simulated translation function (replace with actual translation logic)
std::string translateToEnglish(const char* text) {
    // Implement translation logic here
    // Return the translated text
    return "English translation of " + std::string(text);
}

int main(int argc, char** argv) {
    // Initialize PocketSphinx configuration
    ps_decoder_t* ps = nullptr;
    cmd_ln_t* config = nullptr;
    ad_rec_t* ad = nullptr;

    // Initialize the audio device
    if (ad_open_dev(ad, nullptr, nullptr, DEFAULT_SAMPLES_PER_SEC) < 0) {
        std::cerr << "Failed to open audio device." << std::endl;
        return 1;
    }

    // Initialize PocketSphinx decoder
    config = cmd_ln_init(nullptr, ps_args(), TRUE, nullptr);
    ps = ps_init(config);
    if (!ps) {
        std::cerr << "Failed to initialize PocketSphinx." << std::endl;
        return 1;
    }

    // Set recognition callback
    ps_set_keyphrase_callback(ps, "keyword", recognition_callback, nullptr);

    // Start audio capture and recognition
    if (ad_start_rec(ad) < 0) {
        std::cerr << "Failed to start audio capture." << std::endl;
        return 1;
    }

    // Wait for user input to exit
    std::cout << "Press Enter to exit..." << std::endl;
    std::cin.get();

    // Cleanup and exit
    ad_close(ad);
    ps_free(ps);
    cmd_ln_free_r(config);

    return 0;
}
